# 数据库相关操作，本次大作业的三个任务的查询代码在该文件夹实现
from ADatabase.database import *
import pprint


# 任务一
# 胡云卿、王钲源、李沅城
def missionOne(useID):

    # 初始化数据库连接，获得collections
    tagscollection = Tags()
    tags = tagscollection.getData()

    moviescollection = Movies()
    movies = moviescollection.getData()

    ratingscollection = Ratings()
    ratings = ratingscollection.getData()

    genomescorescollection = GenomeScores()
    gs = genomescorescollection.getData()

    genometagsollection = GenomeTags()
    gt = genometagsollection.getData()

    query = {"tagId": 1}

    for post in gt.find(query):
        pprint.pprint(post)

    result = {}
    item1 = {'num': 1, 'name': 'hello', 'score': 100,
             'tags': [{'tag': 'comedy', 'relevance': 0.8}, {'tag': 'comedy', 'relevance': 0.8},
                      {'tag': 'comedy', 'relevance': 0.8}]}

    item2 = {'num': 2, 'name': 'captain marvel', 'score': 100,
             'tags': [{'tag': 'comedy', 'relevance': 0.8}, {'tag': 'comedy', 'relevance': 0.8},
                      {'tag': 'comedy', 'relevance': 0.8}]}
    item3 = {'num': 3, 'name': "s", 'score': 100,
             'tags': [{'tag': 'comedy', 'relevance': 0.8}, {'tag': 'comedy', 'relevance': 0.8},
                      {'tag': 'comedy', 'relevance': 0.8}]}
    result['data'] = [item1, item2, item3, item3, item3, item3, item3]
    return result


# 任务二
# 徐红莉、潘淑红
def missionTwo():
    pass


# 任务三
# 王硕、刘昱彤
def missionThree():
    pass
