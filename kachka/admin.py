from django.contrib import admin
from .models import Contact,Trainer
#register your models here.

admin.site.register((Trainer,Contact))

