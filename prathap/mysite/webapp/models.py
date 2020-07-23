from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #text=models.TextField()
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
class Rating(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rating_value=models.IntegerField(default=0)
    count=models.IntegerField(default=0)

#OneToOne Relationship

class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=80)
    
    def __str__(self):
        return "%s the place" % self.name
        
class Restaurant(models.Model):
    place=models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs=models.BooleanField(default=False)
    serves_pizza=models.BooleanField(default=False)
    
    def __str__(self):
        return "%s the restaurant" % self.place.name
        
class Waiter(models.Model):
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return "%s the waiter at %s" % (self.name,self.restaurant)
        
#ManyToOne Relationship

class Reporter(models.Model):
        first_name=models.CharField(max_length=30)
        last_name=models.CharField(max_length=30)
        email=models.EmailField()
        
        def __str__(self):
            return "%s %s" % (self.first_name,self.last_name)
            
class Article(models.Model):
    headline=models.CharField(max_length=100)
    pub_date=models.DateField()
    reporter=models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline
        
    class Meta:
        ordering = ['headline']
        
        
#ManyToMany

class Publication(models.Model):
    title=models.CharField(max_length=30)
    
    class Meta:
        ordering=['title']
        
    def __str__(self):
        return self.title
        
class Article2(models.Model):
    headline=models.CharField(max_length=100)
    publications=models.ManyToManyField(Publication)
    
    class Meta:
        ordering=['headline']
        
    def __str__(self):
        return self.headline
        
        
#Model example

class Musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=100)
    
    
class Album(models.Model):
    artist=models.ForeignKey(Musician, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()
    
    
class Person(models.Model):
    SHIRT_SIZES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        )
    name = models.CharField(max_length=60)
    shirt_size=models.CharField(max_length=1,choices=SHIRT_SIZES)
    
'''class Runner(models.Model):
    MedalType=models.TextChoices('MedalType','GOLD SILVER BRONZE')
    name=models.CharField(max_length=60)
    medal=models.CharField(blank=True,choices=MedalType.choices,max_length=10)'''
    
class Fruit(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    
    
class Person2(models.Model):
    name=models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
        
class Group(models.Model):
    name=models.CharField(max_length=128)
    members=models.ManyToManyField(Person2,through='Membership')
    
    def __str__(self):
        return self.name
        
class Membership(models.Model):
    person=models.ForeignKey(Person2,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    date_joined=models.DateField()
    invite_reason=models.CharField(max_length=64)
    
    
class Brand(models.Model):
    name=models.CharField(max_length=100)
    started_at=models.DateField()
    hq_location=models.TextField()
    
    
class Mobile(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    ram=models.IntegerField()
    price_in_inr=models.IntegerField()
    
    
class Student(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    
class Course(models.Model):
    name=models.TextField()
    no_of_credits=models.IntegerField()
    students=models.ManyToManyField(Student)

class Professor(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.TextField()