from django.urls import path
from .views import make_comment, retrive_comments, delete_comment

urlpatterns = [
    path('all/<int:id>/', retrive_comments),
    path('create/', make_comment),
    path('delete/<int:pk>/', delete_comment),
    
]