from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'apps.docs'

router = DefaultRouter()
router.register(r'speciality', views.SpecialityViewSet, basename='speciality')

urlpatterns = [
    path('', include(router.urls)),
]

