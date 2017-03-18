import json
import gzip
import redis
import sys

def main():
    db = redis.Redis(host='localhost', port=6379, db=1)
    for key in db.keys():
        if db.get(key).decode() != 'None':
            print(key.decode() + ": " + db.get(key).decode())

if __name__ == '__main__':
    main()
