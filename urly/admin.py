from django.contrib import admin
from django_urly.models import Url

# Register your models here.
admin.site.register(Url, admin.ModelAdmin)
