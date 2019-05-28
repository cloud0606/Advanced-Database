from django.shortcuts import render
import json
from django.template import loader, Context
from ADatabase.ADatabase.database import *
def hello(request):
    data=movies.objects#tesing
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
def homePage(request):
    # t = loader.get_template('index.html')
    # return t.render()
    return render(request,'index.html')
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

