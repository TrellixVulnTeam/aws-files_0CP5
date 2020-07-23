from django.db import models
from django.utils import timezone
import datetime


'''class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
    
class Question2(models.Model):
    text=models.TextField()
    
class Student(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    
class Course(models.Model):
    name=models.TextField()
    no_of_credits=models.IntegerField()
    students=models.ManyToManyField(Student)
    
class Grades(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    grade=models.CharField(max_length=2)
'''
class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()
    
    def __str__(self):
        return self.name
        
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
        
class Entry(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField()
    authors=models.ManyToManyField(Author)
    number_of_comments=models.IntegerField()
    number_of_pingbacks=models.IntegerField()
    rating=models.IntegerField()
    
    def __str__(self):
        return self.headline
    
    