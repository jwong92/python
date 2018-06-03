# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

# Above, we've imported url and then imported our views
# We have defined a url pattern


# to ensure that we are looking inside THIS urls.py and not the project one:

from django.contrib import admin
from django.conf.urls import include, url
from . import views

app_name = 'mailingsystem'
urlpatterns = [
    # ex: /mailingsystem/
    url(r'^$', views.index, name='index'),
    # ex: /mailingsystem/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /mailingsystem/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /mailingsystem/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]

# Added an include after import on the first line to include our files
# defined a new url for mailingsystem/ - whenever the user requests mailingsystem, it will check the urls.py inside app mailingsystem
