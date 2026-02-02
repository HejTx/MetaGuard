import json, datetime, math

def getInput():
    n = int(input())
    data = []
    for i in range(n):
        data.append(json.loads(input()))
    return data

def main():
    data = getInput()

if __name__ == "__main__":
    main()