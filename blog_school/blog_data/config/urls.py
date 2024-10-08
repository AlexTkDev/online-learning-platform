from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Конфигурация схемы API для Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="List messages from blog",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger ============================================
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Blog ================================================
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/blog/', include('blog.urls')),
]
