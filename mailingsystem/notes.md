# Models

## Creating Models
1. In the app/models.py file, add the following code
```
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
* Each model is represented by a class that subclasses django.db.models.Model
* Each model has class variables which represent a database field in the model
* Each field is represented by instance of Field class (ex. Charfield) to tell Django the type of data each field holds
* Name of each Field instance (ex. question_text, pub_date) is column name
* Optionally use first position argument to a Field to designate a human readable name (ex for pub_date). Otherwise, the machine readable name will be used
* Some fields have required arguments (ex. Charfield requires a max_length)
* Others have optional arguments (ex. votes to 0)

From above, Django will
    1. Create a database schema
    2. Create a python database acess API for accessing these objects

## Activating Models
To include new app in project, add reference to configuration class in INSTALLED_APP setting. The Config class is in the apps.py file, so the dotted path is [name_of_app].apps.[name_of_app]Config
* Django knows how to include the app
* Run `$ python manage.py makemigrations mailingsystem`
* `makemigrations` tells Django there are changes to be implemented from models.
* Migrations can be read from the file `[name_of_app]/migrations/0001_initial.py`
* You can then use the command `migrate` that will run migrations for you and manage database schema automatically.
* Can use the `sqlmigrate` command to take migration names and return their sql
    * `$ python manage.py sqlmigrate [name_of_app] 0001`
    * Note table names are auto generated depending on database being used
    * Primary keys are added automatically
    * Django appends _id to a foreign key field name
    * sqlmigrate doesn't actually run the migration on the database, just prints to screen so see what SQL Django thinks is required. Useful to check.
    * Can also run python manage.py check to check for problems in project
* If everything looks good, run `$ python manage.py migrate`
* Error `Application labels aren't unique, duplicates: mailingsystem` means that in the settings.py, there is a duplicate app name that is under the installed_apps
* migrate command takes all migrations not already applied and runs them against database to sunc the changes made to models with schema in database.
#### 3 Step guide to making model changes
1. Change your models in models.py
2. Run `python manage.py makemigrations` to create migrations for changes
3. Run `python manage.py migrate` to apply the changes to the database

## Playing with the API
* Invoke the python shell with `python manage.py shell`
* Import the model classes just written with 
    * `>>> from [name_of_app].models import [name_of_class] [,name_of_class]`
* Determine the number of question in the system with
    * `>>> Question.objects.all()`
* Create a new question by assigning to a query
* Support for timezones is enabled in default settings, so Django expects a datetime with tzinfo for pub_date
    * `>>> from django.utils import timezone`
    * `>>> q = Question(question_text="What's new?", pub_date=timezone.now())`
* Save the object into the database
    * `>>> q.save()`
* Can find the id with
    * `>>> q.id` -> 1 (or 1L)
* Access model field values with python attributes
    * `>>> q.question_text`
    * `>>> q.pub_date`
* Change values by changing the attribute and calling save
    * `>>> q.question_text = "What's up?"`
    * `>>> q.save()`
* Display all the questions in the database
    * `>>> Question.objets.all()`
    * `>>> exit() or Ctrl-D to exit the shell`
    * This returns an unfriendly representation of the object
    * To fix this, edit the models by adding a `__str__()` method
    * This is a normal python method, but you can also define custom ones
    * ```
        def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        ```
* Run the shell again and import the models
* Running `Question.objects.all()` should now display a human readable form of the qustion
* The API can lookup keyword arguments
    * `>>> Question.objects.filter(id=1)`
    * `>>> Question.objects.filter(question_text__startswith='What')` - note that this is case sensitive
* Get the question that was published this year
    * `>>> from django.utils import timezone`
    * `>>> curent_year = timezone.now().year`
    * `>>> Question.objects.get(pub_date__year=current_year)`
* Requesting an id that doesn't exist raises an exception
* Another way to look up by id is using:
    * `>>> Question.objects.get(pk=1)`
* Use the custom method
    * `>>> q = Question.objects.get(pk=1)`
    * `>>> q.was_published_recently()` - returns true/false

#### Adding to our Choices model
* We can give the question a couple of choices
* The create call constructs a new Choice object, does the insert statement, adds the choice to the set of available choices, and returns the new choice objet
* Django creates a set that holds all foreign key relations to the main class (ex. all choices for the question can be accessed via the API)
    * `>>> q = Question.objects.get(pk=1)`
    * `>>> q.choice_set.all()` - displays all the choices that belong to this question (where choices has the FK)
* Create 3 choices
    * `>>> q.choice_set.create(choice_text='Not much', votes=0`
    * `>>> q.choice_set.create(choice_text='The sky', votes=0`
    * `>>> c = q.choice_set.create(choice_text='The sky', votes=0`
        * NOTE: unsure if choice_set is a standard, or because the model is called choice
* These choice objects now have API access to their related Question objects
    * `>>> c.question` -> <Question: What's up?>
    * `>>> q.choice_set.all()` -> <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
    * `>>> q.choice_set.count()` -> 3
    * API follows relationships as far as needed
    * Use double underscores the separate relationships
    * Find all choices for any question whose pub_date is in this year
```
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Choice.objects.filter(question__pub_date__year=current_year)
```
* returns `<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>` which are all choices created for the question this year

* To delete a choice, use `delete()`
    * `>>> c = q.choice_set.filter(choice_text_startswith='Just hacking')`
    * `>>> c.delete()`
    * Check it's been deleted with
    * `>>> q.choice_set.all()` and `Choice.objects.all()`

## Creating an Admin User
1. `python manage.py createsuperuser`
2. Enter desired username and press enter ex: `Username: admin`
3. Prompted for email address: `Email address: admin@example.com`
4. Enter password twice to confirm: `Password: *********`

### Sart the development server
1. `python manage.py runserver`
2. Open web browser and go to /admin/ to login
3. The admin index page is provided by django.contrib.auth

### Make the app modifiable in the admin
1. The app we created will not be displayed on the admin index page
2. Tell the admin that the model objects have an admin interface
3. Open the __[name_of_app]/admin.py__ file and edit
```
from .models import Question

admin.site.register(Question)
```

## Writing Views Example
* Add views. Here, we define 3 methods. Each of them is a get request that takes in a request and question_id parameter. We return an HttpResponse that is a string, and it takes the URL provided question_id parameter and adds it into the string response

```
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

* Write new views into the [name_of_app].urls with the following paths
```
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /mailingsystem/
    url(r'^$', views.index, name='index'),
    # ex: /mailingsystem/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /mailingsystem/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /mailingsystem/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```
...Note that Django 2 has removed urls and now uses paths

* When somone requests a page (ex. /mailingsystem/34), Django loads the mysite.urls python module, because it is pointed to by ROOT_URLCONF setting. It finds the variable named urlpatterns and traversis the regular expressions in order.

...If it finds the match at __^mailingsystem/__, it will strip off the matching text (__mailingsystem/__) and set the remaining text __34/__ to the mailingsystem.urls URLconf for further processing

...There, it matches `r'^(?P<question_id>[0-9]+)/$'` resulting in a call to the detail() view like `detail(request=<HttpRequest object>, question_id='34')`

...Breaking down `r'^(?P<question_id>[0-9]+)/$'`
* `question_id = '34'` - fromes from `(?P<question_id>[0-9]+)`
    * The parentesis capture the text matching the pattern and sends it as an argument to the view function
* `?P<question_id>` - defines the name that will be used to identify the matched pattern
* `[0-9]+` - is the regular expression to match one or more numbers between 0 and 9

## Writing Views that Do Something
Each view does one of two things
...Return an HTTPResponse object containing the content for the requested pag
...Raising an exception such as Http404

The view can read records from DB, use templates, generate a PDF, JSON, XML, or create zip file using whatever libraries required - as long as it has an HttpResponse or exception.

* Ex - Display latest 5 poll questions in system separated by commas according to publication date in index view in hardcode
```
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```

## Templates
1. Create a directory called __templates__ in the new application directory. Django will look for templates in there.
2. Create a subdirectory with the same name as the application
3. Within the subdirectory, create an index.html file
4. Path to this file is `[app_name]/templates/[app_name]/index.html`
5. Django's app_directories template loader will look for a "templates" subdirectory in each of the installed_apps so to refer to the path in Django, it is simply `polls/index.html`
6. Add code into template
```
{% if latest_question_list %}
<ul>
    {% for question in latest_question_list %}
    <li><a href="/polls/{{question.id}}/">{{question.question_text}}</a></li>
    {% endfor %}
</ul>
{% else %}
    <p>No polls are available</p>
{% endif %}
```
7. Update the [name_of_app]/views.py
```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```
* This code loads the template called [name_of_app]/index.html and passes a context which is a dictionary mapping template variable name to Python object.

### render() shortcut
It is common to load a template, fill a context and return the HttpResponse object with the result of the rendered template. So there is a shortcut
```
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, '[name_of_app]/index.html', context)
```
...Note that if we use render, we no longer need to import loader and HttpResponse. Instead, you import render.
...render() function takes the request object as first argument, a template name as it's second, and a dictionary (aka context) as an optional third. It returns an HttpResponse object of the giventemplate rendered with the given context.

## Raising a 404 Error
In the view, add the following
```
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, '[name_of_app]/detail.html', {'question': question})
```
...The view raises the Http404 exception if a question with the requested ID doesn't exist.

### get_object_or_404() shortcut
If the object doesn't exist, raise an Http404 error. Django provides a shorcut.
* `get_object_or_404()` function takes a Django model as it's first argument, and arbitrary number of keyword arguments which is passed to the __get()__ function of the model manager. It raises Http404 if the object doesn't exist.
```
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
``` 
...Note, we use shortcuts to decouple the model layer to the view layer.
* Can also use __get_list_or_404()__ function that uses __filter()__ instead of __get()__


## Using the Template System
1. Now the view is routed to the [name_of_app]/detail.html, the template might look like this
```
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```
...Template system uses dot-lookup syntax to access variable attributes

...`{{question.question_text}}` does a dictionary lookup on the object question (which was passed from the view that holds the request made to the Question class)

...If it doesn't find the object, it will look for an attribute which it finds in this case

...method-calling occurs in the `{% for %}` loop. __question.choice_set.all__ is the same as __question.choice_set.all()__ method which returns an iterable Choice object and suitable for use

## Remove hardcoded URLs in templates
Defining the url() function in the [name_of_app].urls module, you can remove reliance on a specific URL path defined in the URL configuration using the {% url %} template tag

```urls.py
url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
```

index.html
```
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

...The name value is called by `{% url %}`
...`{% url 'detail' question.id %}` is what produces the link. The __'detail'__ is from the __name='detail'__ in the urls.py 
...If you wanted to change the url of the details view, you can change it in the urls.py like:

```urls.py
url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail')
```
...without changing the template url

## Namespacing URL names
If there were many different apps, you'd have to differentiate between the url names. To do so, add a namespace to the URLconf in each app file.

```[name_of_app]/urls.py
from django.conf.urls import url

from . import views

app_name = 'mailingsystem'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```

...Then update the view url to include the namespace
```
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```



<!-- Spitting out JSON data -->
<!-- https://stackoverflow.com/questions/23110383/how-to-dynamically-build-a-json-object-with-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa -->
<!-- https://www.google.ca/search?q=how+to+product+a+json+string+in+python&oq=how+to+product+a+json+string+in+python&aqs=chrome..69i57.7014j0j7&sourceid=chrome&ie=UTF-8 -->