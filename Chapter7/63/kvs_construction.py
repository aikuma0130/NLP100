import json
import gzip
import redis
import sys

def main():
    db = redis.Redis(host='localhost', port=6379, db=1)
    with gzip.open('../artist.json.gz', 'r') as f:
        for i,line in enumerate(f):
            info = json.loads(line.decode())
            if 'tags' in info:
                db.set(info['name'], info['tags'])
            else:
                db.set(info['name'], None)
    db.save()

if __name__ == '__main__':
    main()
