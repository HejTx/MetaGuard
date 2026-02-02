import pytest, json
from main import is_valid

def test_is_valid():
    transaction = json.loads('{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T15:00:00", "amount": 10.0, "location": {"lat": 34.0522, "lon": -118.2437}, "device_id": "D1"}')
    assert is_valid(transaction) == True
    transaction = json.loads('{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T15:00:15", "amount": 10.0, "location": {"lat": 34.0522, "lon": 118.2437}, "device_id": "D2"}')
    assert is_valid(transaction) == True
    transaction = json.loads('{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T15:00:00", "amount": 10.0, "location": {"lat": -134.0522, "lon": -118.2437}, "device_id": "D1"}')
    assert is_valid(transaction) == False
    transaction = json.loads('{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T15:00:30", "amount": 10.0, "location": {"lat": 134.0522, "lon": -118.2437}, "device_id": "D2"}')
    assert is_valid(transaction) == False
    transaction = json.loads('{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T15:00:00", "amount": 10.0, "location": {"lat": 34.0522, "lon": -218.2437}, "device_id": "D1"}')
    assert is_valid(transaction) == False
    transaction = json.loads('{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T15:00:15", "amount": 10.0, "location": {"lat": 34.0522, "lon": 218.2437}, "device_id": "D1"}')
    assert is_valid(transaction) == False