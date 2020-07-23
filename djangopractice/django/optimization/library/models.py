from django.db import models

# Create your models here.
class Library(models.Model):
    name=models.CharField(max_length=200,default='')
    address=models.CharField(max_length=200,default='')
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=200,default='')
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    library=models.ForeignKey(
        Library, on_delete=models.CASCADE,
        related_name='libraries'
        )
    author=models.ForeignKey(
        Author, on_delete=models.CASCADE,
        related_name='authors'
        )
    title=models.CharField(max_length=200,default='')
    address=models.CharField(max_length=200,default='')
    def get_page_count(self):
        return self.pages.count()
        
    def __str__(self):
        return self.title
        
class Page(models.Model):
    book=models.ForeignKey(
        Book, on_delete=models.CASCADE,
        related_name='pages'
        )
    text=models.TextField(null=True, blank=True)
    page_number=models.IntegerField()
    
class Topping(models.Model):
    name = models.CharField(max_length=30)
    spicy=models.CharField(max_length=30,default=True)
    
    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)
    vegetarian=models.CharField(max_length=30,default=True)
    
    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )
    
class Restaurant(models.Model):
    name=models.CharField(max_length=50)
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by', on_delete=models.CASCADE)