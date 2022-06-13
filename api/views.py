import email
from os import stat
from urllib import response
from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions, status
from rest_framework import viewsets

from .role_permission import IsAdmin, IsUser, IsAmbulance, IsHealthFacility, IsUserOrAmbulance
#from .serializers import UserSerializer
from .models import User, HealthProfile, HealthFacilityAccount, HealthCareFacility, Appointment, UserRating, UserReview, ReviewComment, AmbulanceService, Ambulance, HealthCareService, ClaimRequest, Automations, HeartRateHistory, SleepHistory
#from .models. import Users # This line should be uncommented once the Users class in models.py is uncommented
from .serializers import LoggedInUserSerializer, UserChangePasswordSerializer, UsersSerializer, HealthFacilityAccountSerializer, HealthProfileSerializer, HealthCareFacilitySerializer, AmbulanceSerializer, UserRatingSerializer, UserReviewSerializer, AppointmentSerializer, AutomationsSerializer, ClaimRequestSerializer, SleepHistorySerializer, ReviewCommentSerializer, AmbulanceServiceSerializer, HeartRateHistorySerializer, HealthCareServiceSerializer, NearbyHealthCareFacilitySerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
class UsersViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('firstName')
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserListSerializer
)

class HealthProfileViewSet(viewsets.ModelViewSet):
    queryset = HealthProfile.objects.all()
    serializer_class = HealthProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class HealthFacilityAccountViewSet(viewsets.ModelViewSet):
    queryset = HealthFacilityAccount.objects.all()
    serializer_class = HealthFacilityAccountSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

class HealthCareFacilityViewSet(viewsets.ModelViewSet):
    queryset = HealthCareFacility.objects.all()
    serializer_class = HealthCareFacilitySerializer
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

class AuthUserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)
    



class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'uid': serializer.data['uid'],
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)

class UserListView(APIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated, IsAdmin)

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched logged in users',
            'users': serializer.data

        }
        return Response(response, status=status.HTTP_200_OK)


from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance

class NearbyHealthCareFacilityView(APIView):
    serializer_class = NearbyHealthCareFacilitySerializer
    permission_classes = (IsUserOrAmbulance, ) #(IsUser, IsAmbulance) #(AllowAny,) #todo => is user or ambulance

    def get(self, request):
        limit = int(request.query_params.get('limit',None) or 10)
        max_distance = int(request.query_params.get('max_distance',None) or 3000)
        coord = list(request.query_params['coordinates'].split(","))
        userCoord = Point(float(coord[0]),float(coord[1]), srid=4326)
        res = HealthCareFacility.objects.filter(GPSCoordinates__distance_lte=(userCoord,D(m=max_distance))).annotate(distance=Distance("GPSCoordinates", userCoord)).order_by('distance')[0:limit]
        data = [self.serializer_class(r).data for r in res]
        # serializer = self.serializer_class(data=res.values())
        # valid = serializer.is_valid(raise_exception=True)

        status_code = status.HTTP_200_OK
        response =  {
            'success': True,
            'statusCode': status_code,
            'data': data
        }
        return Response(response, status=status_code)


class LoggedInUserChangePassword(APIView):
    serializer_class = UserChangePasswordSerializer
    permission_classes = (IsAuthenticated, )

    def put(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.update(user, serializer.validated_data)
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Password successfully changed'
            }

            return Response(response, status=status_code)

class LoggedInUserView(APIView):
    serializer_class = LoggedInUserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched logged in users',
            'user': serializer.data

        }
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = User.objects.filter(email=request.user.email)
        serializer.update(user, request.data)
        status_code = status.HTTP_200_OK

        response = {
            'success': True,
            'statusCode': status_code,
            'message': 'User updated successfully',
            'user': serializer.data
        }

        return Response(response, status=status_code)

class AppointmentView(APIView):
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, healthFacilityId, userId):
        try:
            return Appointment.objects.get(user_id=userId,healthFacility_id=healthFacilityId)
        except Appointment.DoesNotExist:
            return []

    def get(self, request, healthFacilityId):
        print(request.user)
        appointments = self.get_object(healthFacilityId, request.user.id)
    
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched appointment',
            'appointments': appointments

        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, healthFacilityId):
        newAppointment = {
            'user': request.user.id,
            'healthFacility': healthFacilityId,
            'dateTime': request.data['dateTime'],
            'status': 'pending',
            'reminderStatus': request.data['reminderStatus'],
        }   
        serializer = self.serializer_class(data=newAppointment)
        valid = serializer.is_valid()

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Appointment successfully created'
            }

            return Response(response, status=status_code)
        
        return Response({'message: "Wrong Data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class CustomJWTokenView(TokenObtainPairView):
#     serializer_class = CustomJWTokenSerializer