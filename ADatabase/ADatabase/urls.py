from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url(r'^$', view.homePage),
    url(r'^query$', view.query),
    url(r'^hello/$', view.hello),
]