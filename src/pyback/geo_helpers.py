"""Geography helpers for coffee finder."""

import geopy.point
from geopy import distance

from .schemas import GeoRect, Point


def dist_km(a: Point, b: Point) -> float:
    """Get km distance between 2 points with lat / lon."""
    return distance.geodesic((a.lat, a.lon), (b.lat, b.lon)).km


# Never lookup more than 100 km
MAX_LOOKUP_KM = 100


def lookup_rect(pivot: Point, km=5) -> GeoRect:
    """Generate lookup rect spanning km around pivot."""
    start = geopy.point.Point(pivot.lat, pivot.lon)
    d = distance.geodesic(kilometers=min(km, MAX_LOOKUP_KM))
    ne = d.destination(point=start, bearing=45)
    sw = d.destination(point=start, bearing=-135)
    return GeoRect(min_lat=sw[0], min_lon=sw[1], max_lat=ne[0], max_lon=ne[1])


def rank(pivot: Point, options: list[Point]) -> list[Point]:
    """Get best matches."""
    return sorted(options, key=lambda op: dist_km(pivot, op))
