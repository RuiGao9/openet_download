from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def plot_timeseries(
    df: pd.DataFrame,
    out_path: str | Path,
    title: str = "OpenET ET",
    show: bool = False,
    figsize: tuple[float, float] = (12, 5),  # width, height in inches
    dpi: int = 300,
    line_color: str = "darkgreen",
    line_width: float = 1.75,
) -> Path:
    out_path = Path(out_path)

    with plt.rc_context({
        "font.family": "serif",
        "font.serif": ["Garamond", "EB Garamond", "Times New Roman", "DejaVu Serif"],
        "font.size": 12,
        "axes.titlesize": 12,
        "axes.labelsize": 12,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
    }):
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)
        ax.plot(df["date"], df["ET_mm"], 
                color=line_color, linewidth=line_width)
        ax.set_title(title)
        ax.set_xlabel("Date")
        ax.set_ylabel("ET (mm)")
        fig.autofmt_xdate()

        fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
        if show:
            plt.show()
        plt.close(fig)

    return out_path