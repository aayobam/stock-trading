from django.urls import path
from . import views

urlpatterns = [
    path('user/dashboard', views.UserDashboardView.as_view(), name="user_dashboard"),
    path('user-graph', views.UserDashboardGraphView.as_view(), name="user_graph"),
    path('admin/dashboard', views.AdminDashboardTradeListView.as_view(), name="admin_dashboard"),
    path('admin-graph', views.AdminDashboardGraphView.as_view(), name="admin_graph"),
]
