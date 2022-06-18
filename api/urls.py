from django.urls import include, path

from . import views
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    AuthUserRegistrationView,
    AuthUserLoginView,
    AppointmentsView,
    AppointmentView,
    LoggedInUserView,
    NearbyHealthCareFacilityView,
    LoggedInUserChangePassword,
    SearchHealthCareFacilityView,
    UserRatingView,
    EmergencyContactsView,
    EmergencyContactView,
)

router = routers.DefaultRouter()
router.register(r'Users', views.UsersViewSet) # This line should be uncommented when the UsersViewSet is uncommented in the views.py
router.register(r'HealthProfile', views.HealthProfileViewSet)
router.register(r'HealthFacilityAccount', views.HealthFacilityAccountViewSet)
router.register(r'healthCareFacility', views.HealthCareFacilityViewSet)
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
    # path('auth/token/obtain/', CustomJWTokenView.as_view(), name='token_create'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), #tested but postman trial...
    path('auth/logout/', jwt_views.TokenBlacklistView.as_view(), name='token_blacklist'), #! cron job flushexpiredtokens...
    path('auth/register', AuthUserRegistrationView.as_view(), name='register'),
    path('auth/login', AuthUserLoginView.as_view(), name='login'),
    path('auth/user', LoggedInUserView.as_view(), name='user'),
    path('auth/user/password', LoggedInUserChangePassword.as_view(), name='password'),


    # search hfs
    path('healthcarefacility/search/', SearchHealthCareFacilityView.as_view(), name="search health care facilities"),

    # nearby hfs
    path('healthcarefacility/nearyby/', NearbyHealthCareFacilityView.as_view(), name='nearby'), #!

    # ratings
        # update/add new rating to health care facility (by logged in user)
        # fetch rating of logged in user to health care facility
    path('rating/<int:healthFacilityId>', UserRatingView.as_view(), name = "upsert rating"),
        # fetch all ratings (all users, all health care facilities for rec) (IsRecServer...?... with api key huh?...)
    # path('ratings/', Ratings.as_view(), name="ratings")    


    # reviews
        # new review to a health care facility (by logged in user) (no 's')
    # path('review/<int:healthFacilityId>')
        # fetch reviews of a health care facility (with 's')
    # path('reviews/<int:healthFacilityId>')

    # appointment view
    path('appointments/<int:healthFacilityId>', AppointmentsView.as_view(), name='appointments'),
    path('appointment/<int:appointmentId>', AppointmentView.as_view(), name='appointment'),
    
    path('emergencycontacts/', EmergencyContactsView.as_view(), name='emergencycontacts'),
    path('emergencycontact/<int:emergencyContactId>', EmergencyContactView.as_view(), name='emergencycontact'),
]
