from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name="accounts"
urlpatterns = [
    path('profile/', views.ProfileView, name="profile"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.RegisterView, name='register_url'),
    path('logout/', LogoutView.as_view(next_page="accounts:login_url"), name="logout"),
]
