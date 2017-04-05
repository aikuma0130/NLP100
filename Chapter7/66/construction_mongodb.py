import json
import gzip
import pprint
import pymongo
from pymongo import MongoClient

def main():
    client = MongoClient('localhost', 27017)
    db = client.artist
    collection = db.artistcolall
    with gzip.open('../artist.json.gz', 'r') as f:
        for line in f:
            info = json.loads(line.decode())
            collection.insert_one(info)
    pprint.pprint(collection.find_one())

if __name__ == '__main__':
    main()
