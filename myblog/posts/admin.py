from django.contrib import admin
from .models import Genre, Post, Comment

admin.site.register(Genre)
admin.site.register(Post)
admin.site.register(Comment)
