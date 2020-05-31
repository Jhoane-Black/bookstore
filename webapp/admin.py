from django.contrib import admin

# Register your models here.
from webapp.model.models import Book

admin.site.register(Book)