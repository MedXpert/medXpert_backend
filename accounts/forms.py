from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from core.models import Users, HealthProfile, Address
from django import forms

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['firstName', 'lastName', 'email', 'phoneNumber', 'username', 'password', 'profilePicture', 'creationDateTime', 'dateOfBirth', 'sex', 'healthProfileID', 'address', 'additionalAttributes']
        USERNAME_FIELD = 'username'

class CreateHealthProfile(ModelForm):
    class Meta:
        model = HealthProfile
        fields = ['healthConditions', 'height', 'weight']

class CreateAddress(ModelForm):
    class Meta:
        model = Address
        fields = ['houseNumber', 'kebele', 'subCity', 'regionOrCity', 'country']