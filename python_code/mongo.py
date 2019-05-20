import pymongo
import datetime
import pprint
# 连接到运行的mongod实例
# client = MongoClient('192.168.56.102', 27017)
# 连接到运行的mongod实例，采用url格式
client = pymongo.MongoClient('mongodb://192.168.56.104:27017/')
# 获取数据库 database
db = client['test_database']
# 获取集合 collection
posts = db['posts'] # 等同于 posts = db.posts

def insert():
    db.post.delete_many({})
    db.profiles.delete_many({})
    print('----------- 插入 Document -----------')
    # 单条数据
    post = {"author": "Mike",
             "text": "My first blog post!",
             "tags": ["mongodb", "python", "pymongo"],
             "date": datetime.datetime.utcnow()
            }
    # 多条数据
    new_posts = [{"author": "Mike",
                  "country":"china",
                  "text": "Another post!",
                  "tags": ["bulk", "insert"],
                  "date": datetime.datetime(2009, 11, 12, 11, 14)},
                  {"author": "Eliot",
                   "country": "china",
                  "title": "MongoDB is fun",
                  "text": "and pretty easy too!",
                  "date": datetime.datetime(2009, 11, 10, 10, 45)}]
    print('单条插入')
    print(posts.insert_one(post).inserted_id)

    print('批量插入')
    result = posts.insert_many(new_posts)
    print(result.inserted_ids)

    # result = posts.insert(new_posts)
    return

def query():
    print('----------- 查询 Document -----------')
    query1 = {"author": "Mike"}
    query2 = {"author": "Eliot"}
    query3 = {"country": "china"}
    #query_id = {"_id": post_id}
    print('满足条件 {"author": "Mike"} 的查询')
    pprint.pprint(posts.find_one(query1))
    print('满足条件 {"author": "Eliot"} 的查询')
    pprint.pprint(posts.find_one(query2))

    print('满足条件 {"country": "china"} 的查询')
    for post in posts.find(query3):
        pprint.pprint(post)
    print('满足条件 {"country": "china"} 的查询一共有：',end='')
    num = posts.count_documents(query1)
    print(num)


def update():
    print('----------- 更新 Document -----------')
    print('更新单个文档')
    query1 = {"author": "Mike"}
    operator1 = {'$set': { 'text': 'this is an update opration' }}
    result = db.posts.update_one(query1,operator1)
    print(result.matched_count)

def delete():
    print('----------- 删除 Document -----------')
    query1 = {"author": "Mike"}
    print('删除满足条件的文档')
    result = db.posts.delete_many(query1)
    print(result.deleted_count)
    #print('仅删除一个满足条件的文档')
    #result = db.posts.delete_one(query1)
    #print(result.deleted_count)
    print('删除所有的文档')
    result= db.posts.delete_many({})
    print(result.deleted_count)

def conditionOperator():
    print('----------- 条件操作符 -----------')
    d1 = datetime.datetime(2009, 11, 12, 12)
    d2 = datetime.datetime(2009, 11, 11, 12)
    # 此处使用了条件操作符
    print('查询2019 11 12 以前的数据')
    for post in posts.find({"date": {"$lt": d1}}).sort("author"):
        pprint.pprint(post)
    print('查询2019 11 11 以前的数据')
    for post in posts.find({"date": {"$lt": d2}}).sort("author"):
        pprint.pprint(post)

    return

def type():
    print('----------- type操作符 -----------')
    print('查询text字段类型为string的document')
    for post in db.posts.find({"text": {'$type': 2}}): # 2 代表string
        pprint.pprint(post)
    return

def limitSkip():
    print('----------- limit skip方法 -----------')
    print('只显示查询结果中的一个')
    for post in db.posts.find({"text": {'$type': 2}}).limit(1): # 2 代表string
        pprint.pprint(post)
    print('跳过2个满足条件的查询结果')
    for post in db.posts.find({"text": {'$type': 2}}).skip(1):
        pprint.pprint(post)

def sort():
    print('----------- 排序 -----------')
    print('按照时间升序排列')
    for post in db.posts.find({"text": {'$type': 2}}).sort('date', pymongo.ASCENDING):
        pprint.pprint(post)
    print('按照时间降序排列')
    for post in db.posts.find({"text": {'$type': 2}}).sort('date', pymongo.DESCENDING):
        pprint.pprint(post)

def index():
    print('----------- 建索引 -----------')
    print('建立索引防止重复数据的插入')
    db.profiles.delete_many({})
    db.profiles.create_index([('user_id', pymongo.ASCENDING)],unique=True)
    print(sorted(list(db.profiles.index_information())))
    print('插入非重复数据数据')
    user_profiles = [{'user_id': 211, 'name': 'Luke'},
                     {'user_id': 212, 'name': 'Ziltoid'}]
    result = db.profiles.insert_many(user_profiles)
    print(result.inserted_ids)

    new_profile = {'user_id': 213, 'name': 'Drew'}
    duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
    result = db.profiles.insert_one(new_profile)
    print(result.inserted_id)
    try :
        print('插入重复数据')
        result = db.profiles.insert_one(duplicate_profile)
        print(result.inserted_id)
    except Exception:
        print('无法插入重复数据')


if __name__ == '__main__':

   #insert()
   query()
  # update()
  # delete()
  # conditionOperator()
   #type()
  # limitSkip()
  # sort()
   #index()