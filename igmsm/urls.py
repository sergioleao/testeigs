"""
URL configuration for igmsm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from department.api.viewset import DepartamentViewset
from department.models import Department
from employer.api.viewset import EmployeeListViewset, EmployeeViewset
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path as url
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="IGS TEST API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)



from employer.models import Employee

route = routers.DefaultRouter()
route.register(r'employeelist', EmployeeListViewset, basename='employeelist',)
route_admin = routers.DefaultRouter()
route_admin.register(r'employee', EmployeeViewset, basename='employee')
route_admin.register(r'department', DepartamentViewset, basename='department')


urlpatterns = [
    path('', include('home.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/admin/', include(route_admin.urls), name='api_admin'),
    path('api/v1/public/', include(route.urls), name='api_public'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
