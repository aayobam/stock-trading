from django.urls import path
from . import views

urlpatterns = [
    path('user/register', views.RegisterAccountView.as_view(), name="register"),
    path('user/login', views.user_login, name="user_login"),
    path('user/logout', views.user_logout, name="user_logout"),
    path('user/dashboard', views.UserDashboardView.as_view(), name="user_dashboard"),
    path('admin/dashboard', views.AdminDashboardTradeListView.as_view(), name="admin_dashboard"),
    path('admin/dashboard/<uuid:id>', views.AdminDashboardTradeDetailView.as_view(), name="admin_dashboard"),
]
