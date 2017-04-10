import pymongo
from pymongo import MongoClient


class ArtistDB(object):
    def __init__(self, address):
        self.client = MongoClient(address, 27017)
        self.db = self.client.artist
        self.collection = self.db.artistcol

    def search(self, name, alias, tag):
        search_query = {}
        if name != '':
            search_query['name'] = { "$eq": name }
        if alias != '':
            search_query['aliases_name'] = { "$in": [alias] }
        if tag != '':
            search_query['tags_value'] = { "$in": [tag] }

        cur = self.collection.find(search_query).sort("rating_value", -1)
        artists = []
        for index, artist in enumerate(cur):
            artists.append(artist)
            if index == 100:
                break

        return artists
        #return [ {'name': search_query} ]
