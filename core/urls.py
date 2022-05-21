from django.urls import include, path
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'authentication'

router = routers.DefaultRouter()
router.register(r'Users', views.UsersViewSet)
router.register(r'HealthProfile', views.HealthProfileViewSet)
router.register(r'Address', views.AddressViewSet)
router.register(r'Admin', views.AdminViewSet)
router.register(r'HealthFacilityAccount', views.HealthFacilityAccountViewSet)
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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]