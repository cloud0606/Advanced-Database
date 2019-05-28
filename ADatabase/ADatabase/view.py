from django.shortcuts import render
from django.template import loader, Context
import pymongo
from mongoengine import *
# 处理数据库连接
client = pymongo.MongoClient('mongodb://62.234.117.231:27017/')
db = client['local']
links = db['links']
movies = db['movies']
ratings = db['ratings']
tags = db['tags']
genome_tags = db['genome_tags']

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def homePage(request):
    # t = loader.get_template('index.html')
    # return t.render()
    return render(request,'index.html')
def searchUser(request):#根据用户ID搜索
    a = {}
    return render(request, '', a=a)
def searchMovie(request):#关键字
    a={}
    return render(request,'',a=a)
def searchTop(request):#top20
    a={}
    return render(request,'',a=a)