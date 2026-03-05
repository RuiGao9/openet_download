from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def plot_timeseries(
    df: pd.DataFrame,
    out_path: str | Path,
    title: str = "OpenET ET",
    show: bool = False,
) -> Path:
    out_path = Path(out_path)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(df["date"], df["ET_mm"])
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("ET (mm)")
    fig.autofmt_xdate()

    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    plt.close(fig)
    return out_path