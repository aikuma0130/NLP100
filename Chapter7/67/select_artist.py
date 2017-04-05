import pymongo
from pymongo import MongoClient
import pprint

def main(*names):
    client = MongoClient('localhost', 27017)
    db = client.artist
    collection = db.artistcol

    for name in names:
        cur = collection.find({'name': name})

        for col in cur:
            pprint.pprint(col)

if __name__ == '__main__':
    main('Queen', 'WIK▲N', 'Priest')
