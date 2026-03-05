from __future__ import annotations
from typing import Any, Literal
import os
import requests
import pandas as pd

from .exceptions import OpenETDownloadError

Interval = Literal["daily", "monthly"]

# OpenET model choices (canonical forms)
Model = Literal["ensemble", "disalexi", "eemetric", "geesebal", "ptjpl", "sims", "ssebop"]

AVAILABLE_MODELS: tuple[str, ...] = (
    "disalexi", "eemetric", "ensemble", "geesebal", "ptjpl", "sims", "ssebop"
)

_MODEL_CANON: dict[str, str] = {
    # already-canonical
    "ensemble": "ensemble",
    "disalexi": "disalexi",
    "eemetric": "eemetric",
    "geesebal": "geesebal",
    "ptjpl": "ptjpl",
    "sims": "sims",
    "ssebop": "ssebop",

    # common user spellings -> canonical
    "pt-jpl": "ptjpl",
    "pt_jpl": "ptjpl",
    "pt jpl": "ptjpl",
    "ptjpl ": "ptjpl",
    "eemetric ": "eemetric",
}

OPENET_POINT_URL = "https://openet-api.org/raster/timeseries/point"

def normalize_model(model: str) -> str:
    key = model.strip().lower()
    canon = _MODEL_CANON.get(key)
    if canon is None:
        raise OpenETDownloadError(
            f"Unknown model '{model}'. Choose one of: {', '.join(AVAILABLE_MODELS)}"
        )
    return canon


def fetch_point_timeseries(
    lon: float,
    lat: float,
    start: str,
    end: str,
    interval: Interval,
    api_key: str | None = None,
    model: str = "Ensemble",
    variable: str = "ET",
    reference_et: str = "gridMET",
    units: str = "mm",
    timeout_s: int = 60,
) -> pd.DataFrame:
    """
    Fetch OpenET time-series for a point.

    Returns a DataFrame with columns: ['date', 'ET_mm'] (+ any extra columns API provides).

    Parameters
    ----------
    model : str
        One of: Ensemble, DisALEXI, eeMETRIC, geeSEBAL, PT-JPL, SIMS, SSEBop
        (case-insensitive; also accepts ptjpl / pt-jpl / eemetric, etc.)
    """
    # API key: prefer argument, fall back to env var
    api_key = api_key or os.getenv("OPENET_API_KEY")
    if not api_key:
        raise OpenETDownloadError(
            "Missing API key. Pass api_key=... or set environment variable OPENET_API_KEY."
        )

    # Normalize model name to canonical OpenET naming
    model = normalize_model(model)

    payload: dict[str, Any] = {
        "date_range": [start, end],
        "interval": interval,
        "geometry": [lon, lat],  # [longitude, latitude]
        "model": model,
        "variable": variable,  # ETa in OpenET wording
        "reference_et": reference_et,
        "units": units,
        "file_format": "JSON",
    }

    headers = {
        "Authorization": api_key,
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    resp = requests.post(
        OPENET_POINT_URL, json=payload, headers=headers, timeout=timeout_s
    )
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        raise OpenETDownloadError(
            f"OpenET API request failed: {e} | body={resp.text[:500]}"
        ) from e

    data = resp.json()

    # Normalize response into records
    if isinstance(data, list):
        records = data
    elif isinstance(data, dict):
        records = data.get("data") or data.get("timeseries") or data.get("values")
        if records is None:
            raise OpenETDownloadError(
                f"Unexpected response keys: {list(data.keys())}"
            )
    else:
        raise OpenETDownloadError(f"Unexpected response type: {type(data)}")

    df = pd.DataFrame(records)

    # Standardize columns
    if "time" in df.columns and "date" not in df.columns:
        df = df.rename(columns={"time": "date"})

    # Find ET value column
    if "value" in df.columns and "ET_mm" not in df.columns:
        df = df.rename(columns={"value": "ET_mm"})
    elif "ET" in df.columns and "ET_mm" not in df.columns:
        df = df.rename(columns={"ET": "ET_mm"})
    elif "et" in df.columns and "ET_mm" not in df.columns:
        df = df.rename(columns={"et": "ET_mm"})

    if "date" not in df.columns or "ET_mm" not in df.columns:
        raise OpenETDownloadError(
            f"Could not identify 'date' and ET column in response. Columns: {list(df.columns)}"
        )

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    return df