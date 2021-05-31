from django import template
from django.db.models import fields, Count
from django.shortcuts import render
from django.template import loader
from .models import *
#week9day1
from django.views import generic
from django.urls import reverse_lazy
from django import forms




class CustomerListView(generic.ListView):
    queryset= Customer.objects.order_by('first_name')
    context_object_name = 'customer_list'

class CustomerCreateView(generic.CreateView):
    model = Customer
    fields= '__all__'
    # fields = ['id', 'first_name', 'last_name', 'phone_number', 'address', 'city', 'country', 'email']
    success_url= reverse_lazy('customer_list') #the url to redirect to if create seccessed

class CustomerDetailView(generic.DetailView):
    model = Customer
    fildes = '__all__'
    
class CustomerUpdateView(generic.UpdateView):
    model = Customer
    fields = '__all__'
    success_url= reverse_lazy('customer_list')

class RentalListView(generic.ListView):
    queryset= Rental.objects.all()
    context_object_name = 'rental_list'

class RentalDetailView(generic.DetailView):
    model = Rental
    fildes = '__all__'

class RentalCreateView(generic.CreateView):
    model= Rental
    fields = ['customer', 'vehicle', 'return_date','rental_date']
    success_url= reverse_lazy('rental_list')

class VehicleListView(generic.ListView):
    queryset = Vehicle.objects.annotate(Count('vehicle_type'))
    context_object_name = 'vehicle_list'

class VehicleDetailView(generic.DetailView):
    model= Vehicle
    fields = '__all__'
    



    



