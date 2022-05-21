# from rest_framework import serializers
# #from .models import User
# from django.contrib.auth.models import User, Group
# from rest_framework import serializers

# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = '__all__'

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


# A new serializer

from django.contrib.auth.models import User, Group
from .models import HealthProfile, Address, Users
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