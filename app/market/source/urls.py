from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Market-service - production',
        default_version='v1',
        description="Api",
    ),
    url=settings.SWAGGER_URL,
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(SessionAuthentication,),
)

urlpatterns = [
    path('api/', include('api.urls')),
    # Service
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path('rosetta/', include('rosetta.urls')),
    # API
    path('api/user/', include('apps.users.urls')),
    path('api/wb/', include('apps.wildberries.urls')),
    path('api/supplier/', include('apps.suppliers.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/warehouses/', include('apps.warehouses.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
