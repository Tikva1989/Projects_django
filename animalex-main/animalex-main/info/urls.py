from django.urls import path
from . import views


urlpatterns = [
    path('animals/', views.all_animals, name='all_animals'),
    path('animal/<int:animal_id>/', views.single_animal, name='single_animal'),
    path('family/<int:family_id>/', views.single_family, name='single_family'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('add_family/', views.add_family, name='add_family'),
    path('add_person/', views.add_person, name='add_person'),
    path('add_passport/', views.add_passport, name='add_passport'),
    path('view_person/<int:person_id>/', views.person_details, name='person_deets'),
    
]

