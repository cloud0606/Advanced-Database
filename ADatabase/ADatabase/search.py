# 数据库相关操作，本次大作业的三个任务的查询代码在该文件夹实现
from ADatabase.database import *


# 任务一
# 胡云卿、王钲源、李沅城
def missionOne():
    ratings = Ratings()
    gs = GenomeScores()
    gt = GenomeTags()
    data1 = gs.genome_scores.find()
    for data in data1:
        print(data.get('tagId'))


# 任务二
# 徐红莉、潘淑红
def missionTwo():
    pass


# 任务三
# 王硕、刘昱彤
def missionThree():
    pass
