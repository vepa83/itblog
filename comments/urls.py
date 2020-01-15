from django.urls import path
from . import views


app_name = 'comments' 
urlpatterns = [
    path('<int:article_id>', views.leavecomment, name='leavecomment'),
    path('<int:comment_id>/deletecomment', views.deletecomment, name='deletecomment'),
]