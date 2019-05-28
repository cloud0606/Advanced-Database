from django.shortcuts import render
from django.template import loader, Context
from ADatabase.database import Mongodb

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def homePage(request):
    # t = loader.get_template('index.html')
    # return t.render()
    return render(request,'index.html')
