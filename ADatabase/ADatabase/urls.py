from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url(r'^$', view.homePage),
    url(r'^query2/$', view.query2),
    url(r'^query1/$', view.query1),
    url(r'^query3/$', view.query3),
    url(r'^hello/$', view.hello),
]