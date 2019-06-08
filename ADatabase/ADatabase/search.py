# # 数据库相关操作，本次大作业的三个任务的查询代码在该文件夹实现
from ADatabase.database import *
import pprint
import pprint
import operator
import time

# 任务一
# 胡云卿、王钲源、李沅城

# 根据用户ID，搜索用户所看的电影名字和评分及评分，按时间从新到旧排序，给出电影的前三个标签及关联度评分
# 目前完成：根据用户ID，搜索用户所看的电影名字和评分及评分，按时间从新到旧排序
# 未完成：给出电影的前三个标签及关联度评分
def missionOne(userId):

    ratings = Ratings()
    tags = Tags()
    genome_scores = GenomeScores()
    genome_tags = GenomeTags()
    movies = Movies()

    movieId = []
    title = []
    rating = []
    dict = []
    timestamp = []
    tag = []
    tagId = []
    relevance = []

    query1 = {"userId": userId}

    # 我们认为这里用户看过的电影就是用户评过等级或者打过tag的电影
    # 得到该用户看过的电影的movieid=tags.movieId+ratings.movieId
    for x in tags.tags.find(query1):
        movieId.append(x["movieId"])
        # dict.append({"movieId": x["movieId"],"timestamp":x ["timestamp"]})
    for x in ratings.ratings.find(query1):
        movieId.append(x["movieId"])
        # dict.append({"movieId": x["movieId"], "timestamp": x["timestamp"]})
    print(movieId)
    # print(dict)


    # 要把重复的 movieId去掉，时间消耗约0.00003，忽略不计
    movieId_remove_duplicate_value = list(set(movieId))
    print(movieId_remove_duplicate_value)


    # 去movies表里面拿到title和rating
    print("=============")
    for y in movieId_remove_duplicate_value:


        query2 = {"movieId": y}
        query3 = {"userId": userId,"movieId": y}

        # # 从tags中得到对应的3个tag
        # # 按时间从新到旧排序，给出电影的前三个标签及关联度评分
        # tag_3 = []
        # tagId_3 = []
        # relevance_3 = []
        #
        # print('按照时间降序排列得到最近的3个tag及关联度评分')
        # tag_result = tags.tags.find(query2)
        # for x in tag_result:
        #     print(x["tag"])
        #     tag_3.append(x["tag"])
        #
        #
        #     query4 = {"tag": x['tag']}
        #     # 得到tagId
        #     for t in genome_tags.genome_tags(query4):
        #         print(t["tagId"])
        #         tagId_3.append(t["tagId"])
        #
        #         # 查relevance
        #         query5 = {"movieId": y, "tagId": t['tagId']}
        #         for z in genome_scores.genome_scores(query5):
        #             print(z["relevance"])
        #             relevance_3.append(z["relevance"])
        #
        # tag.append(tag_3)
        # tagId.append(tagId_3)
        # relevance.append((relevance_3))


        # 得到title
        for x in movies.movies.find(query2):
            title.append(x["title"])

        # 从ratings中得到timestamp
        for x in ratings.ratings.find(query2):
            timestamp.append(x["timestamp"])

        # 得到此movieId的rating
        # 查到result 0.0000n s
        time_start = time.time()
        result = ratings.ratings.find(query3)
        print(result)
        time_end = time.time()
        print("查询result时间消耗：%f" % (time_end - time_start))

        time_start = time.time()
        for x in result:
            time_end = time.time()
            print("遍历ratings表时间消耗：%f" % (time_end - time_start))
            rating.append(x["rating"])
            print(x["rating"])
        # time_end = time.time()
        # print("遍历ratings表时间消耗：%f" % (time_end - time_start))




    print(title)
    print(rating)
    # print(tag)
    # print(tagId)
    # print(relevance)


    # 整理成dict形式
    i = 0
    for x in  movieId_remove_duplicate_value:
        dict.append({"movieId": x, "timestamp":timestamp[i] ,"title":title[i],
                     "rating":rating[i]})
        i = i+1

    print(dict)
    sorted_dict = sorted(dict, key=operator.itemgetter('timestamp'), reverse=True)
    print(sorted_dict)









# 任务二
# 徐红莉、潘淑红
# 根据输入的关键词，查询电影名字里有关键词的电影
def missionTwo(keyword):
    query1 = {"title": {"$regex": keyword,"$options":"i"}}  # 正则表达式,i表示忽略大小写

    movies = Movies()
    title = []
    result = []
    i = 1

    print("======movies-title=======")
    for x in movies.movies.find(query1):
        dict = {"title":x["title"],"num":i}
        i = i + 1
        result.append(dict)


    pprint.pprint(result)
    return result





# 任务三
# 王硕、刘昱彤
# 查询某一风格最受欢迎的20部电影（选做）
# 问题：总共耗时巨长，待优化
def missionThree(type):

    movies = Movies()
    ratings = Ratings()
    links = Links()
    tags = Tags()
    genome_scores = GenomeScores()
    genome_tags = GenomeTags()

    query1 = {"genres": type}
    query3 = {"genres": {"$regex": type,"$options":"i"}}  #正则表达式，i表示忽略大小写
    query4 = {"movieId": 4}
    query5 = {"tagId": 1}
    query6 = {"movieId": 422}


    time_start = time.time()
    print("=======movies======")
    # results = movies.movies.find({query4})
    # print(results)


    # 在movies中得到符合条件的movieId
    movieId = []
    title = []
    i=0

    for x in movies.movies.find(query3):
        movieId.append(x["movieId"])
        i+=1
    print(movieId)
    print(i)
    time_end1 = time.time()
    print(time_end1 - time_start)




    #在ratings表中对每一个movieId求average_rating
    print("=======ratings======")
    movieId_averagerating_list = []
    for x in movieId:
        time_start1 = time.time()
        query7 = {"movieId":x}
        rating = []
        for y in ratings.ratings.find(query7):
            rating.append(y["rating"])

        print(x)
        print(rating)

        time_end2 = time.time()
        print(time_end2 - time_start1)
        # 这一步之前时间消耗很长,主要消耗在从表中查数据的时间，每查一次大概需要9s

        # 求average_ratings
        sum = 0

        # 评分不足10条的，按照0来算
        if (len(rating) <= 10):
            average_rating = 0
        else:
            for y in rating:
                sum += y
            average_rating = sum / len(rating)



        # 保留两位小数
        average_rating = round(average_rating, 2)
        print("average_rating = %.2f" % average_rating)



        # 得到title
        for y in movies.movies.find(query7):
            title = y["title"]

        # 创建字典类型dict
        movieId_averagerating_dict = {"movieId": x, "average_rating": average_rating, "title": title}
        movieId_averagerating_list.append(movieId_averagerating_dict)


    # 根据average_ratings 排序
    sorted_movieId_averageratings_list = sorted(movieId_averagerating_list,
                                                key=operator.itemgetter('average_rating'),
                                                reverse=True)

    account = len(sorted_movieId_averageratings_list)
    print("%s 类型一共有 %d 部电影"%(type,account))
    result = sorted_movieId_averageratings_list[:20]

    # 给result加上序号1-20
    i =  1
    for x in result:
        result[i-1]["num"] = i
        i = i+1


    # 打印最受欢迎的前20部电影
    pprint.pprint(result)

    return result


# if __name__ == '__main__':
#
#     connectDatabase()
#     print("successful--connectDatabase")
#     time_start1 = time.time()
#     # missionOne(1040)
#
#     missionTwo("2016")
#
#     # missionThree("children")
#     time_end2 = time.time()
#     print(time_end2 - time_start1)