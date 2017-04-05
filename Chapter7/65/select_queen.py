import pymongo
from pymongo import MongoClient

def main():
    client = MongoClient('localhost', 27017)
    db = client.artist
    collection = db.artistcol

    cur = collection.find({'name': 'Queen'})

    for col in cur:
        print(col)

if __name__ == '__main__':
    main()
