from django.db import models


class ContactDetail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

