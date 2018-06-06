## Using API to grab JSON

1. In virtual environment, install requests
`$ pip install requests` or `$ easy_install requests`

2. Make a request

```views.py
import requests 

def json_view(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    return HttpResponse(response);
```

...Option to add parameters

```
def json_view(request):
    parameters = {"beer_name": "dark"}
    response = requests.get('https://api.punkapi.com/v2/beers', params=parameters)
    return HttpResponse(response)
```

...Grab properties
```
import json
from pprint import pprint
import requests

def json_view(request):
    parameters = {"beer_name": "dark"}
    response = requests.get('https://api.punkapi.com/v2/beers', params=parameters)    
    return HttpResponse(json.loads(response.content)[0]['name'])
```
* Some key methods to note
    * `json.loads`
    * `json.dumps`
    * `pprint`
    * `response.content`

Define a function with that returns a view with the get response. 

## Model Methods
* Define custom methods on a model to add custom "row-level" functionality 

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)s
```
* The last method is a property.
* `__unicode__()` (equivalent to `__str__()`) is a magic method that returns a unicode representation of any object. Whenever a model needs to be displayed as a plain string.


## Executing custom SQL directly
Access the database directly, routing around the model layer

__django.db.connection__ represents default database connection.
1. Call __connection.cursor()__ to get a cursor object
2. Call __cursor.execute(sql, [params])__ to execute the SQL
3. Use __cursor.fetchone()__ or __cursor.fetchall()__ to return the resulting rows.

```
from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
            row = cursor.fetchone()
    return row
```
* If more than one database is being used, can specify the database name with
```
from django.db import connections
cursor = connections['my_db_alias'].cursor()
```

Default return will be results without field names. To return a dict, use:
```
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]    
```
OR
```
from collections import namedtuple

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])

    return [nt_result(*row) for row in cursor.fetchall()]
```
* This uses __collections.namedtuple()__ which is a tuple-like object with fields accessible by attribute lookup.
    * It is indexable and iterable - results are immutable and acessible by field names or indices

## MySQLdb
1. Run installation `pip install MySQL-python`
2. In views.py `import MySQLdb`



## Resources
1. http://www.pythonforbeginners.com/requests/the-awesome-requests-module