from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'apps.docs'

router = DefaultRouter()
router.register(r'speciality', views.SpecialityViewSet, basename='speciality')
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'information', views.InformationViewSet, basename='information')
router.register(r'document', views.DocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
]
