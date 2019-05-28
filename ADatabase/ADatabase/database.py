import pymongo

# 处理数据库连接
class Mongodb():
    client = pymongo.MongoClient('mongodb://62.234.117.231:27017/')
    db = client['local']
    links = client.links
    movies=client.movies
    ratings=client.ratings
    tags=client.tags
    genome_tags=client.genome_tags
    def userInformations(self,userID):
        pass

    def keyWordMovies(self,keyword):
        pass

    def Top20Movies(self,style):
        pass