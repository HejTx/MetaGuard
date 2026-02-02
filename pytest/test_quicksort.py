import pytest, json, random
from main import quicksort

def test_quicksort():
    data_sorted = [
        {"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T12:00:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"},
        {"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T12:01:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"},
        {"tx_id": "T3", "account_id": "A1", "timestamp": "2023-01-01T12:02:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"},
        {"tx_id": "T4", "account_id": "A1", "timestamp": "2023-01-01T12:03:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"},
        {"tx_id": "T5", "account_id": "A1", "timestamp": "2023-01-01T12:04:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"}
    ]
    data = [
        {"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T12:00:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"},
        {"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T12:01:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"},
        {"tx_id": "T3", "account_id": "A1", "timestamp": "2023-01-01T12:02:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"},
        {"tx_id": "T4", "account_id": "A1", "timestamp": "2023-01-01T12:03:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"},
        {"tx_id": "T5", "account_id": "A1", "timestamp": "2023-01-01T12:04:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"}
    ]
    random.shuffle(data)
    quicksort(data, 0, len(data) - 1)
    
    assert data == data_sorted

    data_sorted = [
        {"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 100.0, "location": {"lat": 40.7128, "lon": -74.0060}, "device_id": "D1"},
        {"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T10:05:00", "amount": 50.0, "location": {"lat": 48.8566, "lon": 2.3522}, "device_id": "D1"},
        {"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T15:00:00", "amount": 10.0, "location": {"lat": 34.0522, "lon": -118.2437}, "device_id": "D1"},
        {"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T15:00:15", "amount": 10.0, "location": {"lat": 34.0522, "lon": -118.2437}, "device_id": "D2"}
    ]
    data = [
        {"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 100.0, "location": {"lat": 40.7128, "lon": -74.0060}, "device_id": "D1"},
        {"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T10:05:00", "amount": 50.0, "location": {"lat": 48.8566, "lon": 2.3522}, "device_id": "D1"},
        {"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T15:00:00", "amount": 10.0, "location": {"lat": 34.0522, "lon": -118.2437}, "device_id": "D1"},
        {"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T15:00:15", "amount": 10.0, "location": {"lat": 34.0522, "lon": -118.2437}, "device_id": "D2"}
    ]
    random.shuffle(data)
    quicksort(data, 0, len(data) - 1)
    
    assert data == data_sorted