from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Конфигурация схемы API для Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Online school API",
        default_version='v1',
        description="List school endpoints",
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
    # Posts ================================================
    path('', include('blog_posts.urls')),

    # School ================================================
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls')),

    # Courses ================================================
    path('api/courses/', include('courses.urls')),

    # Tests ================================================
    path('api/tests/', include('test_and_grade.urls')),

    # Videolessons ================================================
    path('api/videolessons/', include('videolessons.urls')),

]
