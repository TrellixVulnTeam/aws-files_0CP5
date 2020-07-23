from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100, default='hubs')
    last_name = models.CharField(max_length=100, default='ib')
    full_name = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        null=True, blank=True)

    def __str__(self):
        return self.title

# class Publication(models.Model):
#     articles = models.ManyToManyField(Article)
#     name = models.CharField(max_length=100)
