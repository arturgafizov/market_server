from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import RedirectView
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'apps.users'

router = DefaultRouter()
# router.register('user', views.UserModelViewSet, basename='user')


urlpatterns = [
    path('', login_required(RedirectView.as_view(pattern_name='admin:index'))),
    path('current-user/', views.CurrentUserView.as_view(), name='current_user'),
    path('login/', views.LoginView.as_view(), name='api-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]


urlpatterns += router.urls
