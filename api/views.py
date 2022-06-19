
from urllib import response
from certifi import where
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserListSerializer
)
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions, status
from rest_framework import viewsets

from .role_permission import IsAdmin, IsUser, IsAmbulance, IsHealthFacility, IsUserOrAmbulance
#from .serializers import UserSerializer
from .models import User, EmergencyContacts, HealthProfile, HealthFacilityAccount, HealthCareFacility, Appointment, UserRating, UserReview, ReviewComment, AmbulanceService, Ambulance, HealthCareService, ClaimRequest, Automations, HeartRateHistory, SleepHistory
#from .models. import Users # This line should be uncommented once the Users class in models.py is uncommented
from .serializers import LoggedInUserSerializer, AppointmentUpdateSerializer, EmergencyContactsSerializer, UserChangePasswordSerializer, UsersSerializer, HealthFacilityAccountSerializer, HealthProfileSerializer, HealthCareFacilitySerializer, AmbulanceSerializer, UserRatingSerializer, UserReviewSerializer, AppointmentSerializer, AutomationsSerializer, ClaimRequestSerializer, SleepHistorySerializer, ReviewCommentSerializer, AmbulanceServiceSerializer, HeartRateHistorySerializer, HealthCareServiceSerializer, NearbyHealthCareFacilitySerializer, SearchHealthCareFacilitySerializer
import os
from django.conf import settings
from requests import request as req
import logging
from django.db.models import F

REC_API_KEY = os.getenv('RECOMMENDATION_SERVER_API_KEY')
REC_URL = settings.RECOMMENDATION_SERVER_URL

class UsersViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('firstName')
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


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

        checkEmail = User.objects.filter(email=request.data['email'])
        if checkEmail.count() > 0:
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
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


class NearbyHealthCareFacilityView(APIView):
    serializer_class = NearbyHealthCareFacilitySerializer
    permission_classes = (IsUserOrAmbulance, ) #(IsUser, IsAmbulance) #(AllowAny,) #todo => is user or ambulance

    def get(self, request):
        offset = int(request.query_params.get('offset',None) or 0)
        limit = int(request.query_params.get('limit',None) or 10)
        max_distance = int(request.query_params.get('max_distance',None) or 3000)
        coord = list(request.query_params['coordinates'].split(","))
        userCoord = Point(float(coord[0]),float(coord[1]), srid=4326)
        res = HealthCareFacility.objects.filter(GPSCoordinates__distance_lte=(userCoord,D(m=max_distance))).annotate(distance=Distance("GPSCoordinates", userCoord)).order_by('distance')[offset:offset+limit]
        data = [self.serializer_class(r).data for r in res]
        # serializer = self.serializer_class(data=res.values())
        # valid = serializer.is_valid(raise_exception=True)

        status_code = status.HTTP_200_OK
        response = {
            'success': True,
            'statusCode': status_code,
            'data': data
        }
        return Response(response, status=status_code)


class SearchHealthCareFacilityView(APIView):
    serializer_class = SearchHealthCareFacilitySerializer
    permission_classes = (IsUser,)
    def get(self, request):
        status_code = status.HTTP_200_OK
        search_term = request.query_params.get('q',None)
        if search_term in [None, '']:
            return Response({}, status=status_code)
        
        offset = int(request.query_params.get('offset',None) or 0)
        limit = int(request.query_params.get('limit',None) or 10)

        res = HealthCareFacility.objects.filter(name__icontains=search_term)[offset:limit]
        data = [self.serializer_class(r).data for r in res]
        # serializer = self.serializer_class(data=res.values())
        # valid = serializer.is_valid(raise_exception=True)

        response =  {
            'success': True,
            'statusCode': status_code,
            'data': data
        }
        return Response(response, status=status_code)
class UserRatingView(APIView):
    serializer_class = UserRatingSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, healthFacilityId):
        try:
            rating = float(request.data['rating'])
        except:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        ratingPrev = self.get_rating(request.user.id, healthFacilityId)
        if ratingPrev is not None:
            response = {
                'success':False,
                'message': "Rating by the user to the health facility with the given id already exists."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data={
            'healthFacility': healthFacilityId,
            'user': request.user.id,
            'rating': rating
        })
        is_valid = serializer.is_valid()
        if is_valid:
            serializer.save()
            HealthCareFacility.objects.get(pk=int(healthFacilityId)).updateAverageRating(float(rating))
            #to rec server
            full_url = REC_URL + f'rating/{request.user.id}/{healthFacilityId}'
            rs = req('POST', full_url , params={'key': REC_API_KEY}, json = {'rating':rating})
            if rs.status_code != 200:
                logging.debug('POST to Recommendation server failed.', rs.status_code, rs.text)
            
            response = {
                'success':True,
                'message': "You’ve rated this health care facility successfully.",
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response({'success':False}, status.HTTP_400_BAD_REQUEST)
    def get_rating(self, userId,  healthFacilityId):
        res = UserRating.objects.filter(user=userId, healthFacility=healthFacilityId)
        if res.count() == 0:
            return None
        return res[0]
    def get(self, request, healthFacilityId):
        rating = self.get_rating(request.user.id, healthFacilityId)
        if rating is None:
            response = {
                'success':False,
                'message': "No rating by the user for the health facility with the given id."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = {
            'success':True,
            'data':self.serializer_class(rating).data
        }
        return Response(response, status=status.HTTP_200_OK)
    def delete(self, request, healthFacilityId):
        rating = self.get_rating(request.user.id, healthFacilityId)
        if rating is None:
            #note: rec will sync on restart (rating will be useful until then)
            response = {
                'success':False,
                'message': "No rating by the user for the health facility with the given id."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        rating.healthFacility.updateAverageRating(0, updated=True, previous_rating=rating.rating)
        rating.delete()
        response = {
            'success':True,
            'message':"Rating deleted successfully."
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

# class UpdateUserRatingView(APIView):
    # serializer_class = UserRatingSerializer
    # permission_classes = (IsUser,)
    # def put(self, request, ratingId):
    def put(self, request,healthFacilityId):
        try:
            updatedRating = float(request.data['rating'])
        except:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        rating = self.get_rating(request.user.id, healthFacilityId)
        previous_rating = rating.rating
        rating.rating = updatedRating
        rating.save()
        rating.healthFacility.updateAverageRating(rating.rating, updated=True, previous_rating=previous_rating)
        #to rec server
        full_url = REC_URL + f'rating/{request.user.id}/{healthFacilityId}'
        rs = req('PUT', full_url , params={'key': REC_API_KEY}, json = {'rating':updatedRating})
        if rs.status_code != 200:
            logging.debug('POST to Recommendation server failed.', rs.status_code, rs.text)
        response = {
            'success':True,
            'message':"Rating updated successfully."
        }
        return Response(response, status.HTTP_200_OK)

class UserRatingsView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        offset = int(request.query_params.get('offset',None) or 0)
        limit = request.query_params.get('limit',None)
        end = (offset + int(limit)) if limit else limit #else None => [:None]=>[:len]
        key = request.query_params.get('key',None)
        if (key is None) or (key != os.getenv('API_KEY')):
            return Response({'success':False}, status=status.HTTP_401_UNAUTHORIZED)
        rs = UserRating.objects.all().values('rating',healthFacilityID=F('healthFacility'), userID=F('user'))[offset:end]
        response = {
            'success':True,
            'data': rs
        }
        return Response(response, status=status.HTTP_200_OK)

class RecommendationsView(APIView):
    def get(self, request):
        offset = int(request.query_params.get('offset',None) or 0)
        limit = int(request.query_params.get('limit',None) or 10)
        userId = request.user.id
        full_url = REC_URL + f'recommendations/{userId}'
        rs = req('GET', full_url , params={'key': REC_API_KEY, 'offset': offset, 'limit':limit})
        if rs.status_code != 200:
            logging.debug('GET to Recommendation server failed.', rs.status_code, rs.text)
            return Response({'success':False}, status=rs.status_code)
        json = rs.json()
        res = json['data']
        res = [int(i) for i in res]
        result = []
        if len(res) < limit:
            pad = limit - len(res)
            padding = HealthCareFacility.objects.filter(verificationIndexPer10__gte=5).exclude(id__in=res).order_by('-verificationIndexPer10')[:pad] #, id__not_in=res
            padding = [HealthCareFacilitySerializer(h).data for h in padding]
            result.extend(padding)
        res = [HealthCareFacilitySerializer(HealthCareFacility.objects.get(pk=hid)).data for hid in res]
        res.extend(result)
        response = {
            'success':True,
            'data': res
        }
        return Response(response, status.HTTP_200_OK)


class UserReviewView(APIView):
    serializer_class = UserReviewSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, healthFacilityId):
        try:
            review = request.data['review']
        except:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data={
            'healthFacility': healthFacilityId,
            'user': request.user.id,
            'review': review
        })
        is_valid = serializer.is_valid()
        if is_valid:
            serializer.save()
            response = {
                'success':True,
                'message': "You’ve reviewed this health care facility successfully.",
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response({'success':False}, status.HTTP_400_BAD_REQUEST)
    def get_review(self, userId,  healthFacilityId):
        res = UserReview.objects.filter(user=userId, healthFacility=healthFacilityId)
        if res.count() == 0:
            return None
        return res[0]
    def get(self, request, healthFacilityId):
        review = self.get_review(request.user.id, healthFacilityId)
        if review is None:
            response = {
                'success':False,
                'message': "No review by the user for the health facility with the given id."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = {
            'success':True,
            'data':self.serializer_class(review).data
        }
        return Response(response, status=status.HTTP_200_OK)
    def delete(self, request, healthFacilityId):
        review = self.get_review(request.user.id, healthFacilityId)
        if review is None:
            response = {
                'success':False,
                'message': "No review by the user for the health facility with the given id."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        review.delete()
        response = {
            'success':True,
            'message':"Review deleted successfully."
        }
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request,healthFacilityId):
        try:
            updatedReview = request.data['review']
        except:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        review = self.get_review(request.user.id, healthFacilityId)
        review.review = updatedReview
        review.save()
        response = {
            'success':True,
            'message':"Review updated successfully."
        }
        return Response(response, status.HTTP_200_OK)

class UserReviewsView(APIView):
    serializer_class = UserReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, healthFacilityId):
        offset = int(request.query_params.get('offset',None) or 0)
        limit = int(request.query_params.get('limit',None) or 10)
        res = UserReview.objects.filter(healthFacility=healthFacilityId)[offset:offset+limit]
        data = [self.serializer_class(r).data for r in res]
        # serializer = self.serializer_class(data=res.values())
        # valid = serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        response = {
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


class AppointmentsView(APIView):
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, healthFacilityId, userId):
        try:
            return Appointment.objects.get(user_id=userId, healthFacility_id=healthFacilityId)
        except Appointment.DoesNotExist:
            return []

    def get(self, request, healthFacilityId):
        appointments = Appointment.objects.filter(
            healthFacility_id=healthFacilityId, user_id=request.user.id)

        serializer = self.serializer_class(
            [appointment for appointment in appointments], many=True)

        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched appointment',
            'appointments': serializer.data

        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, healthFacilityId):
        try:
            healthFacility = HealthCareFacility.objects.get(
                id=healthFacilityId)
            newAppointment = {
                'user_id': request.user.id,
                'healthFacility_id': healthFacility.id,
                'dateTime': request.data['dateTime'],
                'status': request.data['status'],
                'reminderStatus': request.data['reminderStatus'],
            }
            serializer = self.serializer_class(data=newAppointment)
            valid = serializer.is_valid()
            if valid:
                serializer.create(newAppointment)
                status_code = status.HTTP_201_CREATED

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'Appointed successfully',
                    'user': serializer.data
                }

                return Response(response, status=status_code)
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                    'success': False,
                    'statusCode': status_code,
                    'message': 'Appointment not created',
                    'errors': serializer.errors
                }

                return Response(response, status=status_code)
        except HealthCareFacility.DoesNotExist:
            return Response({"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "message": "Health facility does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class AppointmentView(APIView):
    serializer_class = AppointmentUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, appointmentId):
        try:
            return Appointment.objects.get(id=appointmentId)
        except Appointment.DoesNotExist:
            return Response({"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "message": "Appointment does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, appointmentId):
        try:
            serializer = self.serializer_class(data=request.data)
            valid = serializer.is_valid(raise_exception=True)

            if valid:
                appointment = Appointment.objects.filter(id=appointmentId)
                serializer.update(appointment, serializer.validated_data)
                status_code = status.HTTP_200_OK

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'Appointment updated successfully',
                    'appointment': serializer.data
                }

                return Response(response, status=status_code)
        except Appointment.DoesNotExist:
            return Response({"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "message": "Appointment does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, appointmentId):
        try:
            appointment = self.get_object(appointmentId)
            appointment.delete()
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Appointment deleted successfully'
            }

            return Response(response, status=status_code)
        
        except Appointment.DoesNotExist:
            return Response({"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "message": "Appointment does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class EmergencyContactsView(APIView):
    serializer_class = EmergencyContactsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        type = request.query_params.get('type', None)
        emergencyContact = EmergencyContacts.objects.filter(
            user_id=request.user.id, type=type or 'email')
        serializer = self.serializer_class(
            [emergencyContact for emergencyContact in emergencyContact], many=True)
        # serializer = self.serializer_class(emergencyContact)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched emergency contact',
            'emergencyContact': serializer.data

        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        valid = serializer.is_valid()
        if valid:
            data = request.data
            data['user_id'] = request.user.id
            serializer.create(data)
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Emergency contact created successfully',
                'emergencyContact': serializer.data
            }

            return Response(response, status=status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': False,
                'statusCode': status_code,
                'message': 'Emergency contact not created',
                'errors': serializer.errors
            }

            return Response(response, status=status_code)


class EmergencyContactView(APIView):
    serializer_class = EmergencyContactsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, emergencyContactId):
        try:
            return EmergencyContacts.objects.get(id=emergencyContactId)
        except EmergencyContacts.DoesNotExist:
            return Response({"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "message": "Emergency contact does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, emergencyContactId):

        try:
            serializer = self.serializer_class(data=request.data)
            valid = serializer.is_valid(raise_exception=True)

            if valid:
                emergencyContact = EmergencyContacts.objects.filter(
                    id=emergencyContactId)
                serializer.update(emergencyContact, serializer.validated_data)
                status_code = status.HTTP_200_OK

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'Emergency contact updated successfully',
                    'emergencyContact': serializer.data
                }

                return Response(response, status=status_code)
        except EmergencyContacts.DoesNotExist:
            return Response({"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "message": "Emergency contact does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emergencyContactId):
        try:
            emergencyContact = EmergencyContacts.objects.get(id=emergencyContactId)
            emergencyContact.delete()
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Emergency contact deleted successfully'
            }

            return Response(response, status=status_code)
        except EmergencyContacts.DoesNotExist:
            return Response({"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "message": "Emergency contact does not exist"}, status=status.HTTP_400_BAD_REQUEST)
