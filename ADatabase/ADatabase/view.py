from django.shortcuts import render
import json
from ADatabase.search import missionOne,missionTwo,missionThree


# 首页面
def homePage(request):
    return render(request, 'index.html')

# 测试页面，最后任务完成时删除
def hello(request):
    test=missionOne()
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

# 查询一
def query1(request):
    UserID = request.POST.get('UserID')
    result = {}
    template = 'result1.html'
    if UserID is not None:
        # 查询数据库
        item1 = {'num': 1, 'time': '20180101', 'name': 'hello', 'rating': 100,
                 'tags': [{'tag': 'comedy', 'relevance': 0.8}, {'tag': 'comedy', 'relevance': 0.8},
                          {'tag': 'comedy', 'relevance': 0.8}]}
        item2 = {'num': 2, 'time': '20180201', 'name': 'captain marvel', 'rating': 100,
                 'tags': [{'tag': 'comedy', 'relevance': 0.8}, {'tag': 'comedy', 'relevance': 0.8},
                          {'tag': 'comedy', 'relevance': 0.8}]}
        item3 = {'num': 3, 'time': '20180301', 'name': UserID, 'rating': 100,
                 'tags': [{'tag': 'comedy', 'relevance': 0.8}, {'tag': 'comedy', 'relevance': 0.8},
                          {'tag': 'comedy', 'relevance': 0.8}]}
        result['data'] = [item1, item2, item3, item3, item3, item3, item3]
    return render(request, template, result)

# 查询二
def query2(request):
    KeyWord = request.POST.get('KeyWord')
    result = {}
    template = 'result2.html'
    if KeyWord is not None:
        
        # 查询数据库
        result['data'] = missionTwo(KeyWord)

    return render(request, template, result)

# 查询三
def query3(request):
    Style = request.POST.get('Style')
    result = {}
    template = 'result3.html'

    if Style is not None:
        # 查询数据库
        result['data'] = missionThree(Style)

    return render(request, template, result)


# 根据用户ID进行查询
def userInformations(request):
    _record1 = {}
    return render(request, 'index.html', {'record1': json.dumps(_record1)})


# 关键词查询
def keyWordMovies(request):
    _record2 = {}
    return render(request, 'index.html', {'record2': json.dumps(_record2)})


# 电影风格查询
def Top20Movies(request):
    _record3 = {}
    return render(request, 'index.html', {'record3': json.dumps(_record3)})

