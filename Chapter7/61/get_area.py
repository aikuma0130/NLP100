import json
import gzip
import redis
import sys

class Artist():
    def __init__(self):
        pass

def main(name):
    db = redis.Redis(host='localhost', port=6379, db=0)
    print(db.get(name))

if __name__ == '__main__':
    main(sys.argv[1])
