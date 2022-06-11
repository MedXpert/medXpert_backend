from dataclasses import field
from re import U
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from .models import User, HealthProfile, HealthFacilityAccount, HealthCareFacility, Appointment, UserRating, UserReview, ReviewComment, AmbulanceService, Ambulance, HealthCareService, ClaimRequest, Automations, HeartRateHistory, SleepHistory
#from .models import Users # This line should be uncommented when the Users class in models.py is uncommented
from rest_framework import serializers
from django.contrib.auth.hashers import check_password

# This class should be uncommented when importing Users is uncommented
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class HealthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfile
        fields = "__all__"

# class AddressSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Address
    #     fields = "__all__"

class HealthFacilityAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacilityAccount
        fields = "__all__"

class HealthCareFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCareFacility
        fields = "__all__"

class AppointmentSerializer(serializers.Serializer):
    
    user = serializers.IntegerField(required=False)
    healthFacility = serializers.IntegerField(required=False)
    dateTime = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=True)
    reminderStatus = serializers.CharField(required=True)
    declinedBy = serializers.CharField(required=False)


    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.reminderStatus = validated_data.get('reminderStatus', instance.reminderStatus)
        instance.declinedBy = validated_data.get('declinedBy', instance.declinedBy)
        instance.save()

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

#!
class NearbyHealthCareFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCareFacility
        fields = "__all__"

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'role'
        )

class LoggedInUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'firstName',
            'lastName',
            'email',
            'phoneNumber',
            'dateOfBirth',
            'role'
        ) 
    
    def update(self, instance, validated_data):
        instance.update(**validated_data)

class UserChangePasswordSerializer(serializers.Serializer):
    oldPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)
    
    def update(self, instance, validated_data):
        # check password is correct
        if check_password(validated_data['oldPassword'], instance.password):
            instance.set_password(validated_data['newPassword'])
            instance.save()
            return instance
        raise serializers.ValidationError('Password is incorrect')


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    uid = serializers.UUIDField(read_only=True)

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
                'uid': user.uid,
                'role': user.role,
            }

            return validation
            
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
