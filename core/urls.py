from django.urls import include, path
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'authentication'

router = routers.DefaultRouter()
router.register(r'Users', views.UsersViewSet)
router.register(r'HealthProfile', views.HealthProfileViewSet)
router.register(r'Address', views.AddressViewSet)

urlpatterns = [
    #path('', views.apiView.as_view(), name='api'),
    #path('', views.apiView, name='api'),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #path('users-list/', views.userView.as_view(), name='users-list'),
    #path('users-detail/<str:pk>/', views.detailView.as_view(), name='users-detail'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]