from __future__ import annotations
from pathlib import Path
from typing import Literal, Any
import pandas as pd

from .api import fetch_point_timeseries, Interval
from .io import ensure_out_dir
from .plot import plot_timeseries

def download_et_timeseries(
    lon: float,
    lat: float,
    start: str,
    end: str,
    interval: Interval = "daily",
    out_dir: str | Path = "openet_output",
    filename: str | None = None,
    api_key: str | None = None,
    plot: bool = True,
    show_plot: bool = False,
    model: str = "Ensemble",
) -> dict[str, Any]:
    """
    Download OpenET ET time series (daily or monthly) for a point and save CSV + plot.

    Returns dict with keys: data (DataFrame), csv (path), figure (path or None).
    """
    out_dir = ensure_out_dir(out_dir)

    df: pd.DataFrame = fetch_point_timeseries(
        lon=lon,
        lat=lat,
        start=start,
        end=end,
        interval=interval,
        api_key=api_key,
        model=model,
    )

    if filename is None:
        filename = f"OpenET_{model}_ET_{interval}_{start}_to_{end}_lon{lon:.5f}_lat{lat:.5f}".replace(":", "-")

    csv_path = out_dir / f"{filename}.csv"
    fig_path = out_dir / f"{filename}.png"

    df.to_csv(csv_path, index=False)

    fig_saved = None
    if plot:
        fig_saved = plot_timeseries(
            df=df,
            out_path=fig_path,
            title=f"OpenET {model} ET ({interval})",
            show=show_plot,
        )

    return {
        "data": df,
        "csv": str(csv_path),
        "figure": str(fig_saved) if fig_saved else None,
        "out_dir": str(out_dir),
        "interval": interval,
        "start": start,
        "end": end,
        "lon": lon,
        "lat": lat,
        "model": model,
    }