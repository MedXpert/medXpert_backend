from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from .models import User, HealthProfile, Address, Admin, HealthFacilityAccount, HealthCareFacility, Appointment, UserRating, UserReview, ReviewComment, AmbulanceService, Ambulance, HealthCareService, ClaimRequest, Automations, HeartRateHistory, SleepHistory
from rest_framework import serializers

# This class should be uncommented when importing Users is uncommented
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'firstName',
            'lastName',
            'email',
            'password',
            'role'
        )

    def create(self, validate_data):
        auth_user = User.objects.create_user(**validate_data)
        return auth_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'role'
        )

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }

            return validation
            
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
