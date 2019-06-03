from django.shortcuts import render
import json
from ADatabase.search import missionOne,missionTwo,missionThree


# 首页面
def homePage(request):
    return render(request, 'index.html')

# 测试页面，最后任务完成时删除
def hello(request):
    result=missionOne("1")
    template = 'result1.html'
    return render(request, template, result)

# 查询一
def query1(request):
    UserID = request.POST.get('UserID')
    result = {}
    template = 'result1.html'
    if UserID is not None:
        # 查询数据库
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
    return render(request, template, result)

# 查询二
def query2(request):
    KeyWord = request.POST.get('KeyWord')
    result = {}
    template = 'result2.html'
    if KeyWord is not None:
        # 查询数据库

        item1 = {'num': 1, 'name': 'Avengers'}
        item2 = {'num': 2, 'name': 'Iron Man1'}
        item3 = {'num': 3, 'name': KeyWord}
        result['data'] = [item1, item2, item3, item3, item3, item3, item3]
    return render(request, template, result)

# 查询三
def query3(request):
    Style = request.POST.get('Style')
    result = {}
    template = 'result2.html'
    if Style is not None:
        # 查询数据库
        item1 = {'num': 1, 'name': 'Avengers'}
        item2 = {'num': 2, 'name': 'Black Panther'}
        item3 = {'num': 3, 'name': Style}
        result['data'] = [item1, item2, item3, item3, item3, item3, item3]
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
