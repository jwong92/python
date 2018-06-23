from django.shortcuts import render


# from pprint import pprint

# Create your views here.
import requests
import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from .models import SensorType, Sensor, MeasureType, Entry, Role, User

def index(request):
    return HttpResponse("Berry Face Index Page")

def insert_temp(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    result = SensorType.objects.insert_sensor(json_obj)
    return HttpResponse(result)

def view_json(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    return HttpResponse(json_obj)
    # return render(request, 'bf/view_json.html', {'json': json_obj})

def clear_db(request):
    SensorType.objects.all().delete()
    MeasureType.objects.all().delete()
    return HttpResponse("Cleared")
    
def add_sensor(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    Sensor.objects.add_sensor(json_obj)
    return HttpResponse("All inserted")

def add_entry(request):
    response = requests.get('http://99.225.25.240:8000/webapp/')
    json_obj = response.json()
    Entry.objects.add_entry(json_obj)
    return HttpResponse("Added Entries")

def add_roles(request):
    data = json.loads(open("bf/roles.json").read())
    Role.objects.add_role(data)
    return HttpResponse("Added Roles")

def add_user(request):
    data = json.loads(open("bf/user.json").read())
    User.objects.insert_user(data)
    return HttpResponse("User Added")

def view_token(request):
    token = User.objects.get_token(json.loads(open("bf/user.json").read()))
    return HttpResponse(token)


# @csrf_exempt
def view_token(request):
    if request.method == "POST":
    # token = User.objects.get_token(json.loads(open("berryface/user.json").read()))
        # token = User.objects.get_token(request.POST)
        # return HttpResponse(request.body)

        # IF USING FORM ENCODED DATA, USE REQUEST.POST AND MAKE SURE THAT THE ENCTYPE IS FORM!
        # json_obj = json.dumps(request.POST)

        # BECUASE I AM PASSING A JSON STRING, I WILL RENDER THE BODY, THEN SERIALIZE THE JSON TO A DICT
        json_str = request.body
        json_dict = json.loads(json_str)
        email = json_dict['user'][0]['email']
        password = json_dict['user'][0]['password']

        # CHECK THE CREDENTIALS
        credentials = User.objects.check_cred_get_token(email, password)
        print credentials
        return HttpResponse(json.dumps(credentials))



# Posting JSON in Python without Requests Library

# https://gist.github.com/kennethreitz/1294570


# https://docs.djangoproject.com/en/2.0/ref/models/instances/
# https://docs.djangoproject.com/en/2.0/topics/db/queries/
# https://docs.djangoproject.com/en/2.0/topics/db/queries/