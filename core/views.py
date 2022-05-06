from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from . import models

#@api_view(['GET'])
class apiView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        api_urls = {
            'Users':'/users-list',
            'Update':'/task-update',
            'Delete':'/task-delete',
        }
        content = {'message': 'Hello, World!'}
        return Response(api_urls)
class userView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = models.Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class detailView(APIView):
    permission_classes = (IsAuthenticated,)

    def __init__(self, pk):
        self.pk = pk

    def get(self, request):
        users = models.Users.objects.get(id=pk)
        serializer = UserSerializer(users, many=False)
        return Response(serializer.data)