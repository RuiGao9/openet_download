from __future__ import annotations
from pathlib import Path

def ensure_out_dir(out_dir: str | Path) -> Path:
    p = Path(out_dir).expanduser().resolve()
    p.mkdir(parents=True, exist_ok=True)
    return p