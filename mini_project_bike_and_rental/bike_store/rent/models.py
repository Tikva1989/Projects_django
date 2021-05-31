from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.constraints import CheckConstraint
from django.utils.translation import gettext_lazy as _
from datetime import date


# Create your models here.
class Customer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True,null=True,unique=True)
    phone_number= models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)


class Vehicle(models.Model):
    vehicle_type= models.ForeignKey('VehicleType', on_delete=models.CASCADE)
    real_cost= models.IntegerField(null=False) 
    size = models.ForeignKey('VehicleSize', on_delete=models.CASCADE )


class VehicleType(models.Model):
    name= models.CharField(max_length=40)


class VehicleSize(models.Model):
    name= models.CharField(max_length=30)


class Rental(models.Model):
    rental_date= models.DateField(auto_now_add=False)
    return_date= models.DateField(auto_now_add=False,null=True)
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE )
    vehicle= models.ForeignKey(Vehicle, on_delete=models.CASCADE )

    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['rental_date', 'vehicle'],name='uniqe_rental')
        ]
        order_with_respect_to = 'return_date'
    

class RentalRate(models.Model):
    daily_rate= models.FloatField()
    vehicle_type= models.ForeignKey('VehicleType', on_delete=models.CASCADE )
    vehicle_size= models.ForeignKey('VehicleSize', on_delete=models.CASCADE )

