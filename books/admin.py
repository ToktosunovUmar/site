from django.contrib import admin
from . import models


admin.site.register(models.books_post)
admin.site.register(models.Reviewbook)