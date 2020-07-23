from django.contrib import admin

# Register your models here.
from .models import Place,Restaurant,Waiter,Reporter,Article,Publication,Article2

admin.site.register(Place)
admin.site.register(Restaurant)