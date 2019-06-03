import pymongo
import sys

# 数据库设置
MONGODB_CONFIG = {
    'host': '62.234.117.231',
    'port': 27017,
    'db_name': 'local',
    'username': None,
    'password': None
}


# 数据库连接
class MongoConn(object):
    def __init__(self):
        # connect db
        try:
            self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
            self.db = self.conn[MONGODB_CONFIG['db_name']]
            self.username = MONGODB_CONFIG['username']
            self.password = MONGODB_CONFIG['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True
        except Exception:
            print('Connect Statics Database Fail.')
            sys.exit(1)

    def getDB(self):
        return self.db

# links集合
class Links:

    def __init__(self):
        self.db = MongoConn()
        self.links = self.db.getDB()['links']

    def getData(self):
        return self.links


# tags集合
class Tags:

    def __init__(self):
        self.db = MongoConn()
        self.tags = self.db.getDB()['tags']

    def getData(self):
        return self.tags


# movies集合
class Movies:

    def __init__(self):
        self.db = MongoConn()
        self.movies = self.db.getDB()['movies']

    def getData(self):
        return self.movies

    def print(self):
        data1 = self.movies.find()
        for data in data1:
            print(data.get('title'))


# ratings集合
class Ratings:

    def __init__(self):
        self.db = MongoConn()
        self.ratings = self.db.getDB()['ratings']

    def getData(self):
        return self.ratings


# genome-tags集合
class GenomeTags:

    def __init__(self):
        self.db = MongoConn()
        self.genome_tags = self.db.getDB()['genome_tags']

    def getData(self):
        return self.genome_tags


# genome-scores集合
class GenomeScores:

    def __init__(self):
        self.db = MongoConn()
        self.genome_scores = self.db.getDB()['genome_scores']

    def getData(self):
        return self.genome_scores

