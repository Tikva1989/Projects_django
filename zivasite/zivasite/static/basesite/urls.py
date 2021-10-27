from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('thanks/', views.send_file_to_user, name="thanks"),
    path('about/', views.about, name="about"),
    ]