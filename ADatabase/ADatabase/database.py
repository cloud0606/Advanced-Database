import pymongo
import json
from mongoengine import *
# 处理数据库连接

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