from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions, status
from .serializers import MailSerializer

class MailView(APIView):
    serializer_class = MailSerializer
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)