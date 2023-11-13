from django.contrib import admin
from .models import Auther, Book, Review

# Register your models here.

admin.site.register(Auther)
admin.site.register(Book)
admin.site.register(Review)