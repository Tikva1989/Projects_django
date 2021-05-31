import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "bike_store.settings")
django.setup()

from faker import Faker
from rent.models import Customer, Vehicle, Rental
# from .rent.models import Customer, Vehicle
from random import randint, random

def create_customer(N=10):
    
    fake = Faker()

    for _ in range(N):
        Customer.objects.create(first_name= fake.first_name(),
        last_name = fake.last_name(),
        email = fake.email(),
        phone_number= fake.pyint(min_value=10000000000, max_value=100000000000),
        address = fake.address(),
        city= fake.city(),
        country= fake.city()
        )

# create_customer(10)
# print("DATA IS POPULATAED SUCCESSFULLY")


def create_vehicle(N=20):
    fake = Faker()

    for _ in range(N):
        Vehicle.objects.create(
         real_cost = fake.pyint(min_value=1000, max_value=10000),
         size_id = random.choice([1, 2, 3]),
         vehicle_type_id = random.choice([2, 3, 4, 5])  
        )

# create_vehicle(20)
# print("DATA IS POPULATAED SUCCESSFULLY")
from datetime import date
import random

# def create_rental(N=5):
#     fake = Faker()
  
#     for _ in range(N):
        
        # Rental.objects.create(
          

        # )

# create_rental(5)
# print("DATA IS POPULATAED SUCCESSFULLY")