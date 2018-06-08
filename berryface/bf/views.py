from django.shortcuts import render


# from pprint import pprint

# Create your views here.
import requests
import json
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from .models import Temperature

def index(request):
    return HttpResponse("Berry Face Index Page")

def add_temp(request, bname):
    # temp = Temperature(b_name="shock top", pub_date=timezone.now())
    # temp.save()
    t = Temperature.objects.filter(pk=1)
    return HttpResponse(serializers.serialize("json", t))

def view_json(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    temp = []
    for beer in json_obj:
        for entries in beer['entries']:
            Temperature(b_name="batch1", )
            temp.append(entries['value'])
            
    return HttpResponse(temp)

# https://docs.djangoproject.com/en/2.0/ref/models/instances/
# https://docs.djangoproject.com/en/2.0/topics/db/queries/
# https://docs.djangoproject.com/en/2.0/topics/db/queries/