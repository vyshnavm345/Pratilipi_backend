from django.contrib import admin
from .models import UserAccount, Article, Comment
# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Article)
admin.site.register(Comment)