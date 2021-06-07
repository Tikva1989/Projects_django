from django.urls import path
from . import views
from django.views.generic import DetailView, CreateView





urlpatterns= [
    path('homepage', views.homepage, name= 'homepage'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_gif/', views.add_gif, name='add_gif'),
    path('category/<int:pk>', views.CategoryDetialView.as_view(), name="single_category"),
    path('categories/', views.AllCategoriesListView.as_view(), name='all_categories'),
    path('gif/<int:pk>', views.GifDetialView.as_view(), name="single_gif"),
    path('uploader/', views.UploaderCreateView.as_view(), name="uploder"),
    
  
]
