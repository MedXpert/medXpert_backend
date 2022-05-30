from xml.dom.minidom import Document
from django.urls import include, path
from . import views
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    AuthUserRegistrationView,
    AuthUserLoginView,
    UserListView
)
app_name = 'authentication'

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'HealthProfile', views.HealthProfileViewSet)
router.register(r'Address', views.AddressViewSet)
router.register(r'Admin', views.AdminViewSet)
# router.register(r'HealthFacilityAccount', views.HealthFacilityAccountViewSet)
router.register(r'HealthCareFacilityImage', views.HealthCareFacilityImageViewSet)
router.register(r'HealthCareFacility', views.HealthCareFacilityViewSet)
router.register(r'Appointment', views.AppointmentViewSet)
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
    path('auth/login', AuthUserLoginView.as_view(), name='login'),
    path('auth/user', UserListView.as_view(), name='user')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)