from django.contrib import admin
from django.urls import path, include
from core.views import EmployeeViewSet
from rest_framework import routers

# Generating the URLs through a router and viewsets
router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
