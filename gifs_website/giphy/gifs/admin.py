from django.contrib import admin
from .models import Gif, Category, Uploader


# Register your models here.
admin.site.register(Gif)
admin.site.register(Category)
admin.site.register(Uploader)