# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# Import HttpResponse
# Create a simple method named index that is taking a parameter request and returning an HttpResponse.
# Response is a normal H1 tag with a message

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mailingsystem/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("<h1>Welcome to Mailing system Python Django App</h1>")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'mailingsystem/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
