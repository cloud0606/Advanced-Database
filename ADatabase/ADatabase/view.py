from django.shortcuts import render
import json
from ADatabase.search import missionOne,missionTwo,missionThree



# 首页面
def homePage(request):
    return render(request, 'index.html')

# 查询一
def query1(request):
    UserID = request.POST.get('UserID')
    result = {}
    template = 'result1.html'
    if UserID is not None:
        # 查询数据库
        result['data'] = missionOne(int(UserID))

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

