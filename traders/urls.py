from django.urls import path
from . import views

urlpatterns = [
    path('user/dashboard', views.UserDashboardView.as_view(), name="user_dashboard"),
    path('admin/dashboard', views.AdminDashboardTradeListView.as_view(), name="admin_dashboard"),
    path('admin-graph', views.AdminDashboardGraphView.as_view(), name="admin_graph"),

    #path('admin/dashboard', views.admin_dashboard_trade_list_view, name="admin_dashboard"),
    #path('admin-graph', views.admin_dashboard_graph_view, name="admin_graph"),
]
