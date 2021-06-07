from django.db import models
from django.db.models import constraints, query
from django.urls import reverse



# Create your models here.
        
class Uploader(models.Model):
    name = models.CharField(max_length=100)
    uploader_img = models.ImageField(upload_to= 'media/')

    def __str(self):
        return self.name
    

class Gif(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(null=False )
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)

    def __str__(self):
        return self.title

        
class Category(models.Model):
        name = models.CharField(max_length=100)
        gifs= models.ManyToManyField(Gif,related_name='categories')
       
        def __str__(self):
            return self.name
        





