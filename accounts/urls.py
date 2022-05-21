from django.urls import path
from . import views

urlpatterns = [
    path('createHealthProfile/', views.createHealthProfile, name='createHealthProfile'),
    path('createAddress/', views.createAddress, name='createAddress'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]