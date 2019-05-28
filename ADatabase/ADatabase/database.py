import pymongo
from mongoengine import *
# 处理数据库连接
client = pymongo.MongoClient('mongodb://62.234.117.231:27017/')
db = client['local']
links = db['links']
movies = client.movies
ratings = client.ratings
tags = client.tags
genome_tags = client.genome_tags
a={'movieId':4016}
s=links.find_one(a)
print({s['tmdbId']})
class Mongodb():
    def userInformations(self,userID):
        pass

    def keyWordMovies(self,keyword):
        pass

    def Top20Movies(self,style):
        pass
