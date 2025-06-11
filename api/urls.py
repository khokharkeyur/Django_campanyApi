
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='company')
router.register(r'employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]

# get company employees