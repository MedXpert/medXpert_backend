from django.contrib.auth.models import User, Group
from .models import HealthProfile, Address, Users, Admin, HealthFacilityAccount, HealthCareFacility, Appointment, UserRating, UserReview, ReviewComment, AmbulanceService, Ambulance, HealthCareService, ClaimRequest, Automations, HeartRateHistory, SleepHistory
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class HealthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfile
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

class HealthFacilityAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacilityAccount
        fields = "__all__"

class HealthCareFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCareFacility
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = "__all__"

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = "__all__"

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = "__all__"

class AmbulanceServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbulanceService
        fields = "__all__"

class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = "__all__"

class HealthCareServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCareService
        fields = "__all__"

class ClaimRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimRequest
        fields = "__all__"

class AutomationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automations
        fields = "__all__"

class HeartRateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartRateHistory
        fields = "__all__"

class SleepHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepHistory
        fields = "__all__"
