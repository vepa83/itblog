from django.urls import path
from . import views


app_name="articles"
urlpatterns = [
    path('', views.homeview, name='home'),
    path('<int:id>', views.detailview, name='detailview'),
    path('searchresult/', views.searchview, name="searchview"),
    path('<int:article_id>/a_update/', views.a_update, name='a_update'),
    path('<int:article_id>/a_delete/', views.a_delete, name='a_delete'),
    path('a_create/', views.a_create, name='a_create'),
    path('create_article/', views.create_article, name='create_article'),
    path('<int:article_id>/like/', views.like, name="like"),
    path('<int:article_id>/dislike/', views.dislike, name="dislike"),
    path('category/<int:cat_id>/', views.catview, name="catview"),
    path('<int:article_id>/add_pictures/', views.add_pic_view, name="add_pic_view"),
    path('<int:article_id>/add_pictures/add', views.add_pic_view_2, name="add_pic_view_2"),
    path('<int:picture_id>/delete_picture/', views.delete_pic_view, name="delete_pic_view"),
    path('menu/<int:item_id>/', views.menuitemview, name="menu_item"),

]