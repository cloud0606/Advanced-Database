import pymongo

def myMissionOne(userid):
	list_sum =[]

	#链接数据库
	# client = pymongo.MongoClient('mongodb://169.254.79.112:27017/')
	client = pymongo.MongoClient('mongodb://localhost:27017/')
	db = client['local']
	#首先链接tags表 然后链接rating表
	tags = db["tags"]
	ratings = db["ratings"]
	movies_conn = db["movies"]
	tagid_conn = db["genome_tags"]


	query = {"userId": userid}
	for i in tags.find(query):
		print(i["movieId"],i["timestamp"])
		list_sum.append([i["movieId"],i["timestamp"],-1])

	for j in ratings.find(query):
		list_sum.append([j["movieId"], j["timestamp"], j["rating"]])

	####开始建立字典   进行数据的综合

	#先对数据进行排序  根据movieid进行排序
	result = sorted(list_sum, key=lambda x: (x[0]))

	#输出排序后的列表
	for i in list_sum:
		print(i)

	dict_list = {}  #用于存储字典数据   key => list
	for i in list_sum:
		if i[0] in dict_list.keys():  #如果键已经存在 时间戳取最小值  评分取最大值
			dict_list[i[0]][0] = min(dict_list[i[0]][0],i[1])
			dict_list[i[0]][1] = min(dict_list[i[0]][1], i[2])

		else:                         #如果不存在 直接存储
			dict_list[i[0]] = [i[1],i[2]]

	# #打印获得的字典
	# print("*********************打印出字典的取值**********************")
	# for i in dict_list.keys():
	# 	print(dict_list[i])

	#查询电影名称
	for i in dict_list.keys():
		query_movie_name ={"movieId":i}
		for j in movies_conn.find(query_movie_name):
			dict_list[i].append(j['title'])




	#根据movieid获取 按时间戳从大到小排序   给出分数最高的三个Tag
	geno_score = db["genome_scores"]
	for i in dict_list.keys():   #此处已经只是一个数组[movieid timestamp ratings   tag  revelance】
		query1 = {"movieId": i}
		list_tmp =[]  #用于存储排名前三的tag和分数
		for j in geno_score.find(query1).sort("relevance",-1):
			list_tmp.append([j["tagId"],j["relevance"]])
			if len(list_tmp) == 3: break

		for k in list_tmp:  #存储tagid和revelance排名
			query_tagname = {"tagId": k[0]}
			tagname =[]
			for p in tagid_conn.find(query_tagname):
				tagname.append(p["tag"])
			k[1] = round(k[1],4)   #todo 此处round函数有问题 没有正确执行
			dict_list[i].append([tagname[0],k[1]])
			#dict_list[i].append(k)

		# 打印出排好序的movieid
	print("*******打印出插入的数值*********")
	for i in dict_list.keys():      # timestamp ratings tagid revelance
		print(dict_list[i])



	#此时已经获得  movieid   timestamp 评分  现在根据timestamp进行排序   从大到小排序
	dict_re = sorted(dict_list.items(), key=lambda x: (x[1][0]),reverse=True)
	for i in dict_re:
		print(i)



	list_final =[]
	index = 1
	for i in dict_re:
		dict_re = {}
		dict_re['num'] = index
		index = index+1

		print("******** i = ******* ",i[1])

		dict_re["time"] = i[1][0]
		dict_re["rating"] = i[1][1]
		dict_re["title"] = i[1][2]

		list_inner = []

		index_tmp = 3
		for index_tmp in range(3,6):
			dict_inner ={}
			dict_inner["tag"] = i[1][index_tmp][0]
			dict_inner["relevance"] = i[1][index_tmp][1]
			list_inner.append(dict_inner)

		dict_re["tags_relevance"] = list_inner
		list_final.append(dict_re)


	for i in list_final:
		print(i)
	return list_final

	# item1 = {'num': 1, 'time': '20180101', 'title': 'hello', 'rating': 100,
	#          'tags_relevance': [{'tag': 'comedy', 'relevance': 0.8}, {'tag': 'comedy', 'relevance': 0.8},
	#                   {'tag': 'comedy', 'relevance': 0.8}]}


myMissionOne(26)

















