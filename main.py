import json
import math
from datetime import datetime, timedelta
from collections import deque
import constants
def get_input():
    """
    Read and parse JSON transaction input from stdin.

    The first line specifies the number of transactions. Each following line
    must be a valid JSON object representing a transaction.

    Returns:
        list: A list of parsed transaction dictionaries.

    Raises:
        ValueError: If the number of transactions is outside the allowed range.
    """
    try:
        n = int(input())
        if n < 0 or n > 10000:
            raise ValueError(f"Invalid transaction count: {n}. Must be <0, 10000>.")
        transactions = []
        for i in range(n):
            transactions.append(json.loads(input()))
        return transactions
    except:
        raise ValueError(f"Invalid transaction count. Must be a singe number <0, 10000>.")

def partition(data, left, right):
    """
    Partition helper for quicksort based on transaction timestamps.

    Args:
        data (list): List of transaction dictionaries.
        left (int): Left index of the partition range.
        right (int): Right index of the partition range.

    Returns:
        int: Final index position of the pivot.
    """
    pivot = datetime.fromisoformat(data[right]["timestamp"])
    i = left - 1
    for j in range(left, right):
        if datetime.fromisoformat(data[j]["timestamp"]) <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    
    data[right], data[i + 1] = data[i + 1], data[right]
    return i + 1

def quicksort(data, left, right):
    """
    Sort transactions in-place by timestamp using quicksort.

    Args:
        data (list): List of transaction dictionaries.
        left (int): Left index of the sort range.
        right (int): Right index of the sort range.
    """
    if left < right:
        pivot = partition(data, left, right)

        quicksort(data, left, pivot - 1)
        quicksort(data, pivot + 1, right)
        
def validate_transaction(transaction):
    """
    Validate geographic coordinates of a transaction.

    Args:
        transaction (dict): Transaction data containing location info.

    Returns:
        bool: True if latitude and longitude are valid, False otherwise.
    """
    try:
        lat = float(transaction["location"]["lat"])
        if lat < -90 or lat > 90:
            return False
        lon = float(transaction["location"]["lon"])
        if lon < -180 or lon > 180:
            return False
    except:
        return False
    return True

def haversine(latitude1, longitude1, latitude2, longitude2):
    """
    Calculate the great-circle distance between two geographic points.

    Args:
        latitude1 (float): Latitude of the first point.
        longitude1 (float): Longitude of the first point.
        latitude2 (float): Latitude of the second point.
        longitude2 (float): Longitude of the second point.

    Returns:
        float: Distance between the two points.
    """
    delta_latitude = math.radians(latitude1 - latitude2)
    delta_longitude = math.radians(longitude1 - longitude2)

    a = math.sin(delta_latitude/2)**2 + math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.sin(delta_longitude/2)**2
    distance = 2 * constants.R * math.asin(math.sqrt(a))
    return distance

def get_delta_time(transaction1, transaction2):
    """
    Compute the absolute time difference between two transactions in hours.

    Args:
        transaction1 (dict): First transaction.
        transaction2 (dict): Second transaction.

    Returns:
        float: Time difference in hours.
    """
    time1 = datetime.fromisoformat(transaction1["timestamp"])
    time2 = datetime.fromisoformat(transaction2["timestamp"])
    delta_time = abs(time1 - time2).total_seconds()/constants.HOUR_TO_SEC
    return delta_time

def check_geo_velocity(transaction1, transaction2):
    """
    Determine whether the geographic velocity between two transactions
    exceeds the maximum allowed speed.

    Args:
        transaction1 (dict): First transaction.
        transaction2 (dict): Second transaction.

    Returns:
        bool: True if velocity exceeds the threshold, False otherwise.
    """
    distance = haversine(transaction1["location"]["lat"], transaction1["location"]["lon"], transaction2["location"]["lat"], transaction2["location"]["lon"])
    time = get_delta_time(transaction1, transaction2)

    try:
        return (distance/time) > constants.MAX_SPD
    except ZeroDivisionError:
        return True
    
class FreqSpike:
    """
    Detect transaction frequency spikes within a rolling time window.
    """
    def __init__(self):
        """
        Initialize an empty transaction timestamp queue.
        """
        self.queue = deque()

    def check(self, transaction):
        """
        Check whether the transaction frequency exceeds the allowed limit.

        Args:
            transaction (dict): Transaction data.

        Returns:
            bool: True if a frequency spike is detected, False otherwise.
        """
        time = datetime.fromisoformat(transaction["timestamp"])
        self.queue.append(time)

        cutoff_time = time - timedelta(seconds=constants.WINDOW_TIME)
        while self.queue and self.queue[0] < cutoff_time:
            self.queue.popleft()
            
        return len(self.queue) >= constants.MAX_LENGTH
    
def is_device_stranger(transaction1, transaction2):
    """
    Detect suspicious device switching between transactions.

    Args:
        transaction1 (dict): First transaction.
        transaction2 (dict): Second transaction.

    Returns:
        bool: True if transactions are from different devices within a short time.
    """
    return get_delta_time(transaction1, transaction2) * constants.HOUR_TO_SEC < constants.MAX_DS and transaction1["device_id"] != transaction2["device_id"]

def main():
    transactions = get_input()
    quicksort(transactions, 0, len(transactions) - 1)

    flags = []
    freq_spike = FreqSpike()
    for i in range(len(transactions)):
        if not validate_transaction(transactions[i]):
            continue
        if i > 0 and validate_transaction(transactions[i - 1]) and check_geo_velocity(transactions[i - 1], transactions[i]):
            flag = json.dumps({'tx_id': transactions[i]['tx_id'], 'reason': 'GEO_VELOCITY'})
            flags.append(flag)
        if freq_spike.check(transactions[i]):
            flag = json.dumps({'tx_id': transactions[i]['tx_id'], 'reason': 'FREQ_SPIKE'})
            flags.append(flag)
        if i > 0 and validate_transaction(transactions[i - 1]) and is_device_stranger(transactions[i - 1], transactions[i]):
            flag = json.dumps({'tx_id': transactions[i]['tx_id'], 'reason': 'DEVICE_STRANGER'})
            flags.append(flag)
    print(flags)

if __name__ == "__main__":
    main()