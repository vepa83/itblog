from django.contrib import admin
from . models import Article, Picture, Category, Like, Dislike

admin.site.register(Article)
admin.site.register(Picture)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Dislike)