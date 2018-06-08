from django.db import models

# Create your models here.
from django.db import models

class Temperature(models.Model):
    b_name = models.CharField(max_length=300)
    temp = models.IntegerField('temperature')
    pub_date = models.DateTimeField('date pulled')
    def __str__(self):
        return self.b_name