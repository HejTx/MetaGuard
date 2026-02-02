import json, math
from datetime import datetime, timedelta
import magic

def getInput():
    n = int(input())
    data = []
    for i in range(n):
        data.append(json.loads(input()))
    return data

def haversine(lat1, lon1, lat2, lon2):
    delta_lat = math.radians(lat1 - lat2)
    delta_lon = math.radians(lon1 - lon2)

    a = math.sin(delta_lat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(delta_lon/2)**2
    dis = 2 * magic.R * math.asin(math.sqrt(a))
    return dis

def getDeltaTime(transaction1, transaction2):
    time1 = datetime.fromisoformat(transaction1["timestamp"])
    time2 = datetime.fromisoformat(transaction2["timestamp"])
    delta_time = abs(time1 - time2).total_seconds()/3600
    return delta_time

def getGeoVelocity(transaction1, transaction2):
    dis = haversine(transaction1["location"]["lat"], transaction1["location"]["lon"], transaction2["location"]["lat"], transaction2["location"]["lon"])
    time = getDeltaTime(transaction1, transaction2)

    try:
        return (dis/time) > magic.MAX_SPD
    except ZeroDivisionError:
        return True

def main():
    data = getInput()

    flags = []
    for i in range(1, len(data)):
        if getGeoVelocity(data[i - 1], data[i]):
            flag = json.dumps({'tx_id': data[i]['tx_id'], 'reason': 'GEO_VELOCITY'})
            flags.append(flag)
    print(flags)

if __name__ == "__main__":
    main()