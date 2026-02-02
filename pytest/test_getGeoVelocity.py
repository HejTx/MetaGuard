import pytest, json
from main import getGeoVelocity

def test_getGeoVelocity():
    assert getGeoVelocity(
        json.loads('{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 100.0, "location": {"lat": 40.7128, "lon": -74.0060}, "device_id": "D1"}'), 
        json.loads('{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T10:05:00", "amount": 50.0, "location": {"lat": 48.8566, "lon": 2.3522}, "device_id": "D1"}')
        ) == True
    assert getGeoVelocity(
        json.loads('{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 100.0, "location": {"lat": 40.7128, "lon": -74.0060}, "device_id": "D1"}'), 
        json.loads('{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-02T10:05:00", "amount": 50.0, "location": {"lat": 48.8566, "lon": 2.3522}, "device_id": "D1"}')
        ) == False