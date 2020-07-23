from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=100)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
