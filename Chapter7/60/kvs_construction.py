import json
import gzip
import redis

class Artist():
    def __init__(self):
        pass

def main():
    db = redis.Redis(host='localhost', port=6379, db=0)
    with gzip.open('../artist.json.gz', 'r') as f:
        for line in f:
            info = json.loads(line.decode())
            if 'area' in info:
                db.set(info['name'], info['area'])
            else:
                db.set(info['name'], None)
    db.save()
    print(db.get('Adam Metcalfe'))

if __name__ == '__main__':
    main()
