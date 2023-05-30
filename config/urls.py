from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('users/', include("users.urls")),
    path('traders/', include("traders.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Stock Trading Administration"
admin.site.site_title = "Stock Trading"
admin.site.index_title = "Stock Trade"
