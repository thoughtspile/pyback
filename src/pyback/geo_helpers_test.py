"""Geographic helpers test suite."""
import pytest

from .geo_helpers import dist_km, lookup_rect, rank
from .schemas import Point, PointOfInterestBase

pivot = Point(lat=59.917931, lon=30.286723)
coffee1_pt = Point(lat=59.910373, lon=30.284117)
coffee2_pt = Point(lat=59.924744, lon=30.287771)
coffee1 = PointOfInterestBase(
    **coffee1_pt.model_dump(), title="Sibaristica", description="Coffee factory"
)
coffee2 = PointOfInterestBase(
    **coffee2_pt.model_dump(), title="Reed", description="Coffee and sanwich"
)


def is_close(v1, v2, tol=0.01):
    """Compare numbers allowing tol=0.01 error."""
    return abs(v1 - v2) < tol


@pytest.mark.parametrize(
    "p1,p2,dist",
    [
        (pivot, pivot, 0),
        (pivot, coffee1, 0.85),
        (pivot, coffee2, 0.76),
    ],
)
def test_dist_km(p1, p2, dist):
    """Distance is calculated properly."""
    assert is_close(dist_km(p1, p2), dist)


def test_rank_order():
    """Rank sorts by distance."""
    assert rank(pivot, [coffee1_pt, coffee2_pt]) == [coffee2_pt, coffee1_pt]


def test_rank_schema():
    """Rank preserves extra fields."""
    assert rank(pivot, [coffee1]) == [coffee1]


def test_rank_empty():
    """Rank accepts empty list."""
    assert rank(pivot, []) == []


def test_lookup_rect_empty():
    """Returns empty rect if dist = 0."""
    empty_rect = lookup_rect(pivot, 0)
    assert is_close(empty_rect.min_lat, pivot.lat)
    assert is_close(empty_rect.max_lat, pivot.lat)
    assert is_close(empty_rect.min_lon, pivot.lon)
    assert is_close(empty_rect.max_lon, pivot.lon)


def test_lookup_rect_normal():
    """Rect is normally sized."""
    rect = lookup_rect(pivot, 2)
    assert is_close(rect.min_lat, 59.90523)
    assert is_close(rect.max_lat, 59.93062)
    assert is_close(rect.min_lon, 30.26145)
    assert is_close(rect.max_lon, 30.31201)


def test_lookup_rect_huge():
    """Rect is trimmed to 100km."""
    rect = lookup_rect(pivot, 10000)
    assert is_close(dist_km(pivot, Point(lat=rect.min_lat, lon=rect.min_lon)), 100)
    assert is_close(dist_km(pivot, Point(lat=rect.max_lat, lon=rect.max_lon)), 100)
