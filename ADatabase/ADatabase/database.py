import pymongo
from mongoengine import *
<<<<<<< HEAD
=======
import mongoengine
>>>>>>> 0a5a8114555f10e64876c518551a64d207e6b8bd
# 处理数据库连接
client = pymongo.MongoClient('mongodb://62.234.117.231:27017/')
db=client['local']
links = db.links
tags=db.tags
movies=db.movies
ratings=db.ratings
genome_tags=db.genome_tags
genome_scores=db.genome_scores
connect()
class links(Document):
    movieId=StringField()
    tmdbId=StringField()
    imdbId=StringField()

    meta={'collection':'links'}

class tags(Document):
    userId=StringField()
    movieId=StringField()
    tag=StringField()
    timestamp=StringField()

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
     tag=StringField()
     meta = {'collection': 'genome_tags'}

<<<<<<< HEAD
class Mongodb():

    client = pymongo.MongoClient('mongodb://62.234.117.231:27017/')
    db = client['local']

    # 根据用户ID进行查询
    def userInformations(self,userID):
        _record1 = {}
        return render(request, 'index.html', {'record1': json.dumps(_record1)})
    # 关键词查询
    def keyWordMovies(self,keyword):
        _record2 = {}
        return render(request, 'index.html', {'record2': json.dumps(_record2)})
    # 电影风格查询
    def Top20Movies(self,style):
        _record3 = {}
        return render(request, 'index.html', {'record3': json.dumps(_record3)})
=======
class genome_scores(Document):
    movieId = mongoengine.StringField()
    tagId=mongoengine.StringField()
    relevance=mongoengine.StringField()
>>>>>>> 0a5a8114555f10e64876c518551a64d207e6b8bd
