from django.contrib import admin

# Register your models here.
from . models import Category, Artcile

admin.site.register(Category)
admin.site.register(Artcile)
