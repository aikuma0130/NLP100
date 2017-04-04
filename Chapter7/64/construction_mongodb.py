import json
import gzip
import pprint
import pymongo
from pymongo import MongoClient

def main():
    client = MongoClient('localhost', 27017)
    db = client.artist
    collection = db.artistcol
    with gzip.open('../artist.json.gz', 'r') as f:
        for line in f:
            info = json.loads(line.decode())
            aliases_name = [ alias.get('name', None) for alias in ( info['aliases'] if 'aliases' in info else [] ) ]
            tags_value = [ tag.get('value', None) for tag in ( info['tags'] if 'tags' in info else [] ) ]
            raging_value = info['rating'].get('value', None) if 'rating' in info else None
            artist = {
                'name': info.get('name', None),
                'aliases_name': aliases_name,
                'tags_value': tags_value,
                'rating_value': raging_value,
            }
            collection.insert_one(artist)
    pprint.pprint(collection.find_one())

if __name__ == '__main__':
    main()
