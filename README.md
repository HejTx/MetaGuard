# MetaGuard

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

## Description
**Metaguard** is a high-performance command-line utility designed to ingest raw financial transaction metadata and identify potential fraud using three specific heuristic algorithms: Geo-Velocity violation, Frequency Spike detection, and Device Switching. The system must process chronological sequences of events and output a structured report of flagged transactions. Intermediate developers must demonstrate proficiency in data parsing, geometric calculations (Haversine formula), and state management across a stream of data objects.
## Used Algorithms
### Geo-Velocity Validation
MetaGuard flags a transaction as potentially fraudulent if the speed required to travel from the previous transaction exceeds 800 km/h. The Haversine formula is used to calculate the distance between 2 points on the globe.
### Frequency Spike Detection
MetaGuard flags a transaction if there have been 5 or more transactions from the same account withing a sliding 5-minute window.
### Device Stranger
Metaguard flags a transaction if 2 transactions have been made within 30 seconds from devices with 2 different IDs.
## Installation and Usage
### Requirements
Python 3.10+
### Installation
#### 1. Clone the repository

```bash
git clone https://github.com/HejTx/MetaGuard.git
cd MetaGuard
```
#### 2. Setup a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
#### 3. Try it out!

```bash
python main.py < demo_input.txt
```
### Usage
#### Input
Input is read from STDIN. The first line contains an integer N (1 <= N <= 10000), representing the number of transaction records. The following N lines each contain a single valid JSON string representing a transaction. Each JSON object contains: 'tx_id' (string), 'account_id' (string), 'timestamp' (string in ISO 8601 format: YYYY-MM-DDTHH:MM:SS), 'amount' (float), 'location' (object with 'lat' and 'lon' floats), and 'device_id' (string). The transactions are not guaranteed to be sorted by timestamp.
#### Output
Output is a single JSON array of objects printed to STDOUT. Each object in the array represents a flagged transaction and includes 'tx_id' and 'reason'. The 'reason' must be one of: 'GEO_VELOCITY', 'FREQ_SPIKE', or 'DEVICE_STRANGER'. The array is sorted primarily by timestamp and secondarily by reason.
#### Parameter modification
All magic constants are stored in constants.py. They can be modified to any realistic value

```python
#Approximate average radius of the earth (in km)
R = 6371

#Limit speed for GEO_VELOCITY flag (in km/h)
MAX_SPD = 800

#Frequency spike sliding window timeframe (in seconds)
WINDOW_TIME = 5 * 60

#Frequency spike maximum number of transactions in window
MAX_LENGTH = 5

#Seconds in an hour
HOUR_TO_SEC = 3600

#Max time between transactions needed to flag as DEVICE_STRANGER (in sec)
MAX_DS = 30
```
#### Examples
```bash
#In:
2
{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T10:00:00", "amount": 100.0, "location": {"lat": 40.7128, "lon": -74.0060}, "device_id": "D1"}
{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T10:05:00", "amount": 50.0, "location": {"lat": 48.8566, "lon": 2.3522}, "device_id": "D1"}
#Out:
['{"tx_id": "T2", "reason": "GEO_VELOCITY"}']
```
```bash
#In:
5
{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T12:00:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"}
{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T12:01:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"}
{"tx_id": "T3", "account_id": "A1", "timestamp": "2023-01-01T12:02:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"}
{"tx_id": "T4", "account_id": "A1", "timestamp": "2023-01-01T12:03:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"}
{"tx_id": "T5", "account_id": "A1", "timestamp": "2023-01-01T12:04:00", "amount": 1.0, "location": {"lat": 0.0, "lon": 0.0}, "device_id": "D1"}
#Out:
['{"tx_id": "T5", "reason": "FREQ_SPIKE"}']
```
```bash
#In:
2
{"tx_id": "T1", "account_id": "A1", "timestamp": "2023-01-01T15:00:00", "amount": 10.0, "location": {"lat": 34.0522, "lon": -118.2437}, "device_id": "D1"}
{"tx_id": "T2", "account_id": "A1", "timestamp": "2023-01-01T15:00:15", "amount": 10.0, "location": {"lat": 34.0522, "lon": -118.2437}, "device_id": "D2"}
#Out:
['{"tx_id": "T2", "reason": "DEVICE_STRANGER"}']
```
