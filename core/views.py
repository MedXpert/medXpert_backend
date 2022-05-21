from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import viewsets
#from .serializers import UserSerializer
from .models import Users, HealthProfile, Address
from .serializers import UsersSerializer, AddressSerializer, HealthProfileSerializer

#@api_view(['GET'])
# class apiView(APIView):
#     permission_classes = (IsAuthenticated,)
    
#     def get(self, request):
#         api_urls = {
#             'Users':'/users-list',
#             'Update':'/task-update',
#             'Delete':'/task-delete',
#         }
#         content = {'message': 'Hello, World!'}
#         return Response(api_urls)
# class userView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         users = models.Users.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
# class detailView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def __init__(self, pk):
#         self.pk = pk

#     def get(self, request):
#         users = models.Users.objects.get(id=pk)
#         serializer = UserSerializer(users, many=False)
#         return Response(serializer.data)

class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('firstName')
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]

class HealthProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HealthProfile.objects.all()
    serializer_class = HealthProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]