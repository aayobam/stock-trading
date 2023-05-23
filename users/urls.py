from django.urls import path
from .import views


urlpatterns = [
    path('register', views.RegisterAccountView.as_view(), name="create_account"),
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout"),
]