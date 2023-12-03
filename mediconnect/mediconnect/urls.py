from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^filer/', include('filer.urls')),
    path("accounts/", include("accounts.urls")),
     path('', home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
