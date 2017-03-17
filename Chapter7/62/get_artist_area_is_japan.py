import json
import gzip
import redis
import sys

class Artist():
    def __init__(self):
        pass

def main():
    db = redis.Redis(host='localhost', port=6379, db=0)
    for key in db.keys():
        if db.get(key).decode() == 'Japan':
            print(key.decode())

if __name__ == '__main__':
    main()
