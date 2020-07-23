from django.db import models
from django.contrib.auth.models import AbstractUser

class myUser(AbstractUser):
    name = models.CharField(max_length=200)
    #date_of_birth = models.DateTimeField()
# Create your models here.
