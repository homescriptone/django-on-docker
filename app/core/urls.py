from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="owise API",
      default_version='v1',
      description="Documentation of the API",
      terms_of_service="https://homescritpone.com",
      contact=openapi.Contact(email="emmanuel.adekplovi@homescriptone.com"),
      license=openapi.License(name="Private Licence"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', include('users.urls') ),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
