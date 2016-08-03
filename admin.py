from django.contrib import admin
from urlshortener import models
# Register your models here.
admin.site.register(models.Url)
admin.site.register(models.WordList)