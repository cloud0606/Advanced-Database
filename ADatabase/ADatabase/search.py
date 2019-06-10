# # 数据库相关操作，本次大作业的三个任务的查询代码在该文件夹实现
from ADatabase.database import *
import pprint
import operator
import time

# 任务一
# 根据用户ID，搜索用户所看的电影名字和评分及评分，按时间从新到旧排序，给出电影的前三个标签及关联度评分
def missionOne(userId):
    # client = pymongo.MongoClient('mongodb://localhost:27017/')
    # db = client.local
    # tags = db.tags


    ratings = Ratings()
    tags = Tags()
    genome_scores = GenomeScores()
    genome_tags = GenomeTags()
    movies = Movies()


    movieId = []
    title = []
    rating = []
    result = []
    timestamp = []
    tag = []
    tagId = []
    relevance = []

    dict_tag_relevance = {}
    list_dict_tag_relevance = []
    query1 = {"userId":userId }


    # 得到movieId
    for y in ratings.ratings.find(query1):
        movieId.append(y["movieId"])
        print("执行7")
        print(y["movieId"])

    # for x in tags.tags.find(query1):
    #     movieId.append(x["movieId"])
    #     print("执行8")
    #     print(x["movieId"])
    print("movieId---------",movieId)



    # 要把重复的 movieId去掉，时间消耗约0.00003，忽略不计
    movieId_remove_duplicate_value = list(set(movieId))
    print("movieId_remove_duplicate_value:")
    print(movieId_remove_duplicate_value)



    # 整理成dict形式
    i = 0
    for x in  movieId_remove_duplicate_value:

        query2 = {"movieId": x}
        query3 = {"movieId": x,"userId": userId}

        # 得到title
        for y in movies.movies.find(query2):
            title.append(y["title"])
            # print("y = ",y)
        # 从ratings中得到timestamp
        for y in ratings.ratings.find(query2):
            timestamp.append(y["timestamp"])

        # 得到此movieId的rating
        for y in ratings.ratings.find(query3):
            rating.append(y["rating"])
            print(y["rating"])


        # 得到tagId和relevance 并排序，得到前三个  形式如：{'relevance': 0.036250000000000004, 'tag': 805}
        query4 = {"movieId": x}
        for y in genome_scores.genome_scores.find(query4):
            r = y["relevance"]
            r = round(r, 4)

            query5 = {"tagId": y["tagId"]}
            for z in genome_tags.genome_tags.find(query5):

                dict_tag_relevance = {"tag":z["tag"],"relevance":r}
            list_dict_tag_relevance.append(dict_tag_relevance)
        sorted_list_dict_tag_relevance = sorted(list_dict_tag_relevance,
                                                key=operator.itemgetter('relevance'),reverse=True)  # 降序

        tag_relevance = sorted_list_dict_tag_relevance[:3]


        #"timestamp":
        result.append({"timestamp": timestamp[i], "title": title[i],
                       "rating": rating[i], "tags_relevance": tag_relevance})
        # result.append({ "timestamp":"qqqqqq","title":title[i],
        #              "rating":100,"tags_relevance":tag_relevance})
        i = i+1

    pprint.pprint(result)
    sorted_result = sorted(result, key=operator.itemgetter('timestamp'), reverse=True)


    # 给result加上序号
    i =  1
    for x in sorted_result:
        sorted_result[i-1]["num"] = i
        i = i+1

    pprint.pprint(sorted_result)

    item1 = [{'num': 1, 'timestamp': '20180101', 'title': 'hello', 'rating': 100,
             'tags_relevance': [{'tag': 'comedy', 'relevance': 0.8}, {'tag': 'comedy', 'relevance': 0.8},
                                {'tag': 'comedy', 'relevance': 0.8}]}]
    pprint.pprint(item1)

    return sorted_result

    # return item1




# 任务二
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
# 查询某一风格最受欢迎的20部电影（选做）
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
#     pprint.pprint(missionOne(13))
#
#     # missionTwo("2016")
#
#     # missionThree("children")
#     time_end2 = time.time()
#     print(time_end2 - time_start1)