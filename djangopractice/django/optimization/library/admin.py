from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Page)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Restaurant)