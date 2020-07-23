from django.db import models
from django.db.models import *

# Create your models here.
class Reporter(models.Model):
    name=models.CharField(max_length=1000)
    stories_field=models.IntegerField(default=0)
    salary=models.IntegerField()
    hike=models.IntegerField()
    
    def __str__(self):
        return self.name