
from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_index, name="article_index"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<category>/", views.article_category, name="article_category"),
]