from django.shortcuts import render,render_to_response
from django.template import loader, Context
from ADatabase.database import Mongodb

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
    return render(request, 'index.html')

