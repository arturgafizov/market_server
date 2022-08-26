from django.urls import path, include

app_name = 'v1'

urlpatterns = [
    path('testing/', include('api.v1.testing.urls'))
]
