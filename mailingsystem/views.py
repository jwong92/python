# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

# Import HttpResponse
# Create a simple method named index that is taking a parameter request and returning an HttpResponse.
# Response is a normal H1 tag with a message

# from pprint import pprint
import json
from pprint import pprint
import datetime
import requests
# from django.http import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.core import serializers
import MySQLdb
# from django.http import JsonResponse
from .models import Question, Choice, Beer
from django.db import connection

class IndexView(generic.ListView):
    template_name = 'mailingsystem/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'mailingsystem/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'mailingsystem/results.html'

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('mailingsystem/index.html')
#     context = {
#         'latest_question_list' : latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#     # return HttpResponse("<h1>Welcome to Mailing system Python Django App</h1>")

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'mailingsystem/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'mailingsystem/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    # Redisplay the form
        return render(request, 'mailingsystem/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('mailingsystem:results', args=(question.id,)))

def json_view(request):
    parameters = {"beer_name": "dark"}
    response = requests.get('https://api.punkapi.com/v2/beers', params=parameters)
    # return HttpResponse(json.dumps(response))
    # return HttpResponse(response)
    # return render(request, 'mailingsystem/json_view.html', {'json': json.loads(response)})
    # return HttpResponse(response.content)
    return HttpResponse((json.loads(response.content), request))
    
    # return HttpResponse(json.loads(response.content)[0]['name'])

def get_beer(request):
    # GET ALL BEER OBJECTS
    # beer = Beer.objects.all()
    # return HttpResponse(beer);

    # GET SPECIFIC BEER NAME
    beer = Beer.objects.all()
    data = serializers.serialize("json", beer)
    return HttpResponse(data);


# from .models import Foo

# def some_name(request):
#     foo_instance = Foo.objects.create(name='test')
#     return render(request, 'some_name.html.html')


# https://stackoverflow.com/questions/6720121/serializing-result-of-a-queryset-with-json-raises-error?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa