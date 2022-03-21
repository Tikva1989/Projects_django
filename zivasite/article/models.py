from tkinter import CASCADE
from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=60)
   


class Article(models.Model):
    title= models.CharField(max_length=255)
    body= models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories= models.ManyToManyField('Category', related_name='articles')
    image= models.ImageField()
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.CharField(max_length=60)
    body=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    article= models.ForeignKey('Article', on_delete=models.CASCADE)


