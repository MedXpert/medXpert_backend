from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'authentication'

urlpatterns = [
    path('', views.apiView.as_view(), name='api'),
    #path('', views.apiView, name='api'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users-list/', views.userView.as_view(), name='users-list'),
    path('users-detail/<str:pk>/', views.detailView.as_view(), name='users-detail'),
]