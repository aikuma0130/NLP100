import json
import gzip
import pymongo
from pymongo import MongoClient

def main():
    client = MongoClient('localhost', 27017)
    db = client.artist
    collection = db.artistcol
    with gzip.open('../artist.json.gz', 'r') as f:
        for line in f:
            info = json.loads(line.decode())
            artist = {
                'name': info.get('name', None),
                'aliases_name': info.get('aliases.name', None),
                'tags_value': info.get('tags.value', None),
                'rating_value': info.get('rating.value', None)
            }
            collection.insert_one(artist)
    print(collection.find_one())

if __name__ == '__main__':
    main()
