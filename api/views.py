from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import viewsets
#from .serializers import UserSerializer
from .models import HealthProfile, Address, Admin, HealthFacilityAccount, HealthCareFacility, Appointment, UserRating, UserReview, ReviewComment, AmbulanceService, Ambulance, HealthCareService, ClaimRequest, Automations, HeartRateHistory, SleepHistory
#from .models. import Users # This line should be uncommented once the Users class in models.py is uncommented
from .serializers import AdminSerializer, HealthFacilityAccountSerializer, AddressSerializer, HealthProfileSerializer, HealthCareFacilitySerializer, AmbulanceSerializer, UserRatingSerializer, UserReviewSerializer, AppointmentSerializer, AutomationsSerializer, ClaimRequestSerializer, SleepHistorySerializer, ReviewCommentSerializer, AmbulanceServiceSerializer, HeartRateHistorySerializer, HealthCareServiceSerializer
#from .serializers import UsersSerializer # This line should be uncommented when UsersSerializer is uncommented in the serializers.py file

# The code below should be uncommented once the above import is uncommented
# class UsersViewSet(viewsets.ModelViewSet):

#     queryset = Users.objects.all().order_by('firstName')
#     serializer_class = UsersSerializer
#     permission_classes = [permissions.IsAuthenticated]

class HealthProfileViewSet(viewsets.ModelViewSet):

    queryset = HealthProfile.objects.all()
    serializer_class = HealthProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('firstName')
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]

class HealthFacilityAccountViewSet(viewsets.ModelViewSet):
    queryset = HealthFacilityAccount.objects.all()
    serializer_class = HealthFacilityAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

class HealthCareFacilityViewSet(viewsets.ModelViewSet):
    queryset = HealthCareFacility.objects.all()
    serializer_class = HealthCareFacilitySerializer
    permission_classes = [permissions.IsAuthenticated]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRatingViewSet(viewsets.ModelViewSet):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserReviewViewSet(viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewCommentViewSet(viewsets.ModelViewSet):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AmbulanceServiceViewSet(viewsets.ModelViewSet):
    queryset = AmbulanceService.objects.all()
    serializer_class = AmbulanceServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class AmbulanceViewSet(viewsets.ModelViewSet):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class HealthCareServiceViewSet(viewsets.ModelViewSet):
    queryset = HealthCareService.objects.all()
    serializer_class = HealthCareServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClaimRequestViewSet(viewsets.ModelViewSet):
    queryset = ClaimRequest.objects.all()
    serializer_class = ClaimRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

class AutomationsViewSet(viewsets.ModelViewSet):
    queryset = Automations.objects.all()
    serializer_class = AutomationsSerializer
    permission_classes = [permissions.IsAuthenticated]

class HeartRateHistoryViewSet(viewsets.ModelViewSet):
    queryset = HeartRateHistory.objects.all()
    serializer_class = HeartRateHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

class SleepHistoryViewSet(viewsets.ModelViewSet):
    queryset = SleepHistory.objects.all()
    serializer_class = SleepHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

