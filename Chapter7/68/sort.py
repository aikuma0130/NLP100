import pymongo
from pymongo import MongoClient
import pprint

def main():
    client = MongoClient('localhost', 27017)
    db = client.artist
    collection = db.artistcol

    cur = collection.find({ "tags_value": { "$in": ['dance'] } }).sort("rating_value", -1)
    for col in cur:
        pprint.pprint(col)

if __name__ == '__main__':
    main()
