import pymongo
from mongoengine import *
import mongoengine

# 数据库连接函数
def connectDatabase():
    client = pymongo.MongoClient('mongodb://62.234.117.231:27017/')
    db = client['local']
    # links = db.links
    # tags = db.tags
    # movies = db.movies
    # ratings = db.ratings
    # genome_tags = db.genome_tags
    # genome_scores = db.genome_scores
    return db

class links(Document):
    movieId = StringField()
    tmdbId = StringField()
    imdbId = StringField()

    meta = {'collection': 'links'}


class tags(Document):
    userId = StringField()
    movieId = StringField()
    tag = StringField()
    timestamp = StringField()

    meta = {'collection': 'tags'}


class movies(Document):

    # 处理数据库连接
    movieId = StringField()
    title = StringField()
    genres = StringField()

    meta = {'collection': 'movies'}

    def print(self):
        db=connectDatabase()
        genome_scores=db.genome_scores
        data1=genome_scores.find()
        for data in data1:
            print(data.get('tagId'))



class ratings(Document):
    movieId = StringField()
    userId = StringField()
    rating = StringField()
    timestamp = StringField()

    meta = {'collection': 'ratings'}


class genome_tags(Document):
    tagId = StringField()
    tag = StringField()
    meta = {'collection': 'genome_tags'}


class genome_scores(Document):
    movieId = mongoengine.StringField()
    tagId = mongoengine.StringField()
    relevance = mongoengine.StringField()
