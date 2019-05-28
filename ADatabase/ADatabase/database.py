import pymongo
from mongoengine import *
import mongoengine

# 处理数据库连接
client = pymongo.MongoClient('mongodb://62.234.117.231:27017/')
db = client['local']
links = db.links
tags = db.tags
movies = db.movies
ratings = db.ratings
genome_tags = db.genome_tags
genome_scores = db.genome_scores
connect()


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
    movieId = StringField()
    title = StringField()
    genres = StringField()

    meta = {'collection': 'movies'}


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
