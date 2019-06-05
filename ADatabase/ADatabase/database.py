import pymongo
from mongoengine import *
import mongoengine

import pymongo
import sys

# # 数据库连接函数
def connectDatabase():
    # client = pymongo.MongoClient('mongodb://62.234.117.231:27017/')
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['local']
    return db


# links集合
class Links:
    movieId = StringField()
    tmdbId = StringField()
    imdbId = StringField()

    meta = {'collection': 'links'}

    def __init__(self):
        self.db = connectDatabase()
        self.links = self.db.links


# tags集合
class Tags:
    userId = StringField()
    movieId = StringField()
    tag = StringField()
    timestamp = StringField()

    meta = {'collection': 'tags'}

    def __init__(self):
        self.db = connectDatabase()
        self.tags = self.db.tags


# movies集合
class Movies:
    # 处理数据库连接
    movieId = StringField()
    title = StringField()
    genres = StringField()

    meta = {'collection': 'movies'}



    def __init__(self):
        self.db = connectDatabase()
        self.movies = self.db.movies
        print(self.movies)


    def print(self):
        db = connectDatabase()
        genome_scores = db.genome_scores
        data1 = genome_scores.find()
        for data in data1:
            print(data.get('tagId'))


# ratings集合
class Ratings:
    movieId = StringField()
    userId = StringField()
    rating = StringField()
    timestamp = StringField()

    meta = {'collection': 'ratings'}

    def __init__(self):
        self.db = connectDatabase()
        self.ratings = self.db.ratings


# genome-tags集合
class GenomeTags:
    tagId = StringField()
    tag = StringField()
    meta = {'collection': 'genome_tags'}

    def __init__(self):
        self.db = connectDatabase()
        self.genome_tags = self.db.genome_tags


# genome-scores集合
class GenomeScores:
    movieId = mongoengine.StringField()
    tagId = mongoengine.StringField()
    relevance = mongoengine.StringField()

    def __init__(self):
        self.db = connectDatabase()
        self.genome_scores = self.db.genome_scores







# import pymongo
# import sys

# # 数据库设置
# MONGODB_CONFIG = {
#     'host': '62.234.117.231',
#     'port': 27017,
#     'db_name': 'local',
#     'username': None,
#     'password': None
# }


# # 数据库连接
# class MongoConn(object):
#     def __init__(self):
#         # connect db
#         try:
#             self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
#             self.db = self.conn[MONGODB_CONFIG['db_name']]
#             self.username = MONGODB_CONFIG['username']
#             self.password = MONGODB_CONFIG['password']
#             if self.username and self.password:
#                 self.connected = self.db.authenticate(self.username, self.password)
#             else:
#                 self.connected = True
#         except Exception:
#             print('Connect Statics Database Fail.')
#             sys.exit(1)

#     def getDB(self):
#         return self.db

# # links集合
# class Links:

#     def __init__(self):
#         self.db = MongoConn()
#         self.links = self.db.getDB()['links']

#     def getData(self):
#         return self.links


# # tags集合
# class Tags:

#     def __init__(self):
#         self.db = MongoConn()
#         self.tags = self.db.getDB()['tags']

#     def getData(self):
#         return self.tags


# # movies集合
# class Movies:

#     def __init__(self):
#         self.db = MongoConn()
#         self.movies = self.db.getDB()['movies']

#     def getData(self):
#         return self.movies

#     def print(self):
#         data1 = self.movies.find()
#         for data in data1:
#             print(data.get('title'))


# # ratings集合
# class Ratings:

#     def __init__(self):
#         self.db = MongoConn()
#         self.ratings = self.db.getDB()['ratings']

#     def getData(self):
#         return self.ratings


# # genome-tags集合
# class GenomeTags:

#     def __init__(self):
#         self.db = MongoConn()
#         self.genome_tags = self.db.getDB()['genome_tags']

#     def getData(self):
#         return self.genome_tags


# # genome-scores集合
# class GenomeScores:

#     def __init__(self):
#         self.db = MongoConn()
#         self.genome_scores = self.db.getDB()['genome_scores']

#     def getData(self):
#         return self.genome_scores

