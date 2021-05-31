from django.urls import path
from . import views


urlpatterns = [
    path('customer/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer/add', views.CustomerCreateView.as_view(), name='customer_add'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='singl_customer'),
    path('customer/update/<int:pk>',views.CustomerUpdateView.as_view(), name= "customer_update" ),
    path('rental/', views.RentalListView.as_view(), name='rental_list'),
    path('rental/<int:pk>', views.RentalDetailView.as_view(), name='rental_detail'),
    path('rental/add', views.RentalCreateView.as_view(), name='rental_add'),
    path('vehicle/', views.VehicleListView.as_view(), name='vehicle_list'),
]
