from django.shortcuts import render
import json
from django.template import loader, Context
import ADatabase.database


def hello(request):
    data = ADatabase.database.movies() # tesing
    context = {}
    data.print()
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def query(request):
    UserID = request.POST.get('UserID') 
    KeyWord = request.POST.get('KeyWord') 
    Style = request.POST.get('Style')    
    result = {}
    template =  'result.html'
    if UserID is not None :
        # 查询数据库
        template = 'result.html'
        item1 = {'num':1,'name':'1','score':100,'tags':['comedy','soft','lazy']}
        item2 = {'num':2,'name':'1','score':100,'tags':['handsome','soft','lazy']}
        item3 = {'num':3,'name':UserID,'score':100,'tags':['tall','soft','lazy']}
        result['data'] = [item1,item2,item3]
    return render(request,template,result)


def homePage(request):
    # t = loader.get_template('index.html')
    # return t.render()
    return render(request, 'index.html')


# 根据用户ID进行查询
def userInformations(request):
    _record1 = {}
    return render(request, 'index.html', {'record1': json.dumps(_record1)})


# 关键词查询
def keyWordMovies(request):
    _record2 = {}
    return render(request, 'index.html', {'record2': json.dumps(_record2)})

    # 电影风格查询

def homePage(request):
    return render(request, 'index.html')

def Top20Movies(request):
    _record3 = {}
    return render(request, 'index.html', {'record3': json.dumps(_record3)})
