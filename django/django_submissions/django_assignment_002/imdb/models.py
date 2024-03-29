from django.db import models

# Create your models here.

    
class Actor(models.Model):
    actor_id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    
    
class Director(models.Model):
    name=models.CharField(max_length=100,unique=True)
    
  
  
class Movie(models.Model):
    name=models.CharField(max_length=100)
    movie_id=models.CharField(max_length=100,primary_key=True)
    box_office_collection_in_crores=models.FloatField()
    release_date=models.DateField()
    #director
    director=models.ForeignKey(Director, on_delete=models.CASCADE)
    actors=models.ManyToManyField(Actor,through='Cast')
    

  
class Cast(models.Model):
    actor=models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    role=models.CharField(max_length=50)
    is_debut_movie=models.BooleanField(default=False)
    
    
class Rating(models.Model):
    movie=models.OneToOneField(Movie,on_delete=models.CASCADE,primary_key=True)
    rating_one_count=models.IntegerField(default=0)
    rating_two_count=models.IntegerField(default=0)
    rating_three_count=models.IntegerField(default=0)
    rating_four_count=models.IntegerField(default=0)
    rating_five_count=models.IntegerField(default=0)