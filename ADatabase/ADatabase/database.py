import pymongo
from mongoengine import *
# 处理数据库连接

class Mongodb():
    # 根据用户ID进行查询
    def userInformations(self,userID):
        _record1 = {}
        return render(request, '', {'_record1': _record1})

    # 关键词查询
    def keyWordMovies(self,keyword):
        _record2 = {}
        return render(request, '', {'_record2': _record2})

    # 电影风格查询
    def Top20Movies(self,style):
        _record3 = {}
        return render(request, '', {'_record3': _record3})
