from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
        path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]