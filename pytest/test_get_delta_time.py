import pytest, json
from main import get_delta_time

def test_get_delta_time():
    assert get_delta_time(
        json.loads('{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 100.0, "location": {"lat": 40.7128, "lon": -74.0060}, "device_id": "D1"}'), 
        json.loads('{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T10:05:00", "amount": 50.0, "location": {"lat": 48.8566, "lon": 2.3522}, "device_id": "D1"}')
        ) == 1/12
    assert get_delta_time(
        json.loads('{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 100.0, "location": {"lat": 40.7128, "lon": -74.0060}, "device_id": "D1"}'), 
        json.loads('{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 50.0, "location": {"lat": 48.8566, "lon": 2.3522}, "device_id": "D1"}')
        ) == 0
    assert get_delta_time(
        json.loads('{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 100.0, "location": {"lat": 40.7128, "lon": -74.0060}, "device_id": "D1"}'), 
        json.loads('{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-02T10:00:00", "amount": 50.0, "location": {"lat": 48.8566, "lon": 2.3522}, "device_id": "D1"}')
        ) == 24