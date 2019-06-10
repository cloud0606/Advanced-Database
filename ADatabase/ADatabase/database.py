import pymongo
from mongoengine import *
import mongoengine

import pymongo

# # 数据库连接函数
def connectDatabase():
    # client = pymongo.MongoClient('mongodb://169.254.79.112:27017/')      # 服务器地址
    client = pymongo.MongoClient('mongodb://localhost:27017/')              # 本地地址
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





