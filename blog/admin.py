from django.contrib import admin
from .models import Post, Comment, SubCategory

admin.site.register(SubCategory)
admin.site.register(Post)
admin.site.register(Comment)