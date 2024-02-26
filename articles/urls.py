from django.urls import path
from .views import Retrive_articles, Retrive_article, add_article, delete_article

urlpatterns = [
    path('all/', Retrive_articles),
    path('add/', add_article),
    path('<int:pk>/', Retrive_article),
    path('delete/<int:pk>/', delete_article),
    
    
]