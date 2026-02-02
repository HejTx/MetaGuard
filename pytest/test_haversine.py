import pytest
from main import haversine

def test_haversine():
    assert round(haversine(15, 50, 0, 0)) == 5740
    assert round(haversine(23.254, 120, -15, 23)) == 11358
    assert round(haversine(0, 0, 0, 0)) == 0
    assert round(haversine(40.7128, -74.0060, 48.8566, 2.3522)) == 5837