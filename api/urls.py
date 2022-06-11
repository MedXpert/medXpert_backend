from django.urls import include, path
from . import views
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    AuthUserRegistrationView,
    AuthUserLoginView,
    AppointmentView,
    LoggedInUserView,
    NearbyHealthCareFacilityView,
    LoggedInUserChangePassword
)

router = routers.DefaultRouter()
router.register(r'Users', views.UsersViewSet) # This line should be uncommented when the UsersViewSet is uncommented in the views.py
router.register(r'HealthProfile', views.HealthProfileViewSet)
router.register(r'HealthFacilityAccount', views.HealthFacilityAccountViewSet)
router.register(r'HealthCareFacility', views.HealthCareFacilityViewSet)
router.register(r'UserRating', views.UserRatingViewSet)
router.register(r'UserReview', views.UserReviewViewSet)
router.register(r'ReviewComment', views.ReviewCommentViewSet)
router.register(r'AmbulanceService', views.AmbulanceServiceViewSet)
router.register(r'Ambulance', views.AmbulanceViewSet)
router.register(r'HealthCareService', views.HealthCareServiceViewSet)
router.register(r'ClaimRequest', views.ClaimRequestViewSet)
router.register(r'Automations', views.AutomationsViewSet)
router.register(r'HeartRateHistory', views.HeartRateHistoryViewSet)
router.register(r'SleepHistory', views.SleepHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register', AuthUserRegistrationView.as_view(), name='register'),
    path('healthcarefacility/nearyby/', NearbyHealthCareFacilityView.as_view(), name='nearby'), #!
    path('auth/login', AuthUserLoginView.as_view(), name='login'),
    path('auth/user', LoggedInUserView.as_view(), name='user'),
    path('auth/user/password', LoggedInUserChangePassword.as_view(), name='password'),

    # appointment view
    path('appointments/<int:healthFacilityId>', AppointmentView.as_view(), name='appointment'),
]
