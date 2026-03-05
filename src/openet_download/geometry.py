from __future__ import annotations
from typing import Tuple, Union, List, Dict, Any

LonLat = Tuple[float, float]
Coords = Union[LonLat, List[LonLat]]

def to_geojson(coords: Coords) -> Dict[str, Any]:
    # Point (lon, lat)
    if isinstance(coords, tuple) and len(coords) == 2:
        lon, lat = coords
        return {"type": "Point", "coordinates": [lon, lat]}

    # Polygon ring (list of lon/lat)
    ring = list(coords)  # type: ignore[arg-type]
    if len(ring) < 4:
        raise ValueError("Polygon needs at least 4 points (including closing point).")

    if ring[0] != ring[-1]:
        ring.append(ring[0])

    return {"type": "Polygon", "coordinates": [[list(pt) for pt in ring]]}