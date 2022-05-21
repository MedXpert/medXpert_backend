from xml.dom import ValidationErr
from django.forms import ModelForm, ValidationError, modelform_factory
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from core.models import Users, HealthProfile, Address, Admin, HealthFacilityAccount, HealthCareFacility, Appointment, UserRating, UserReview, ReviewComment, AmbulanceService, Ambulance, HealthCareService, ClaimRequest, Automations, HeartRateHistory, SleepHistory
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
        password1 = 'password'
        password2 = 'password'

        # def clean_password2(self):
        #     password1 = self.cleaned_data['password1']
        #     password2 = self.cleaned_data['password2']
        #     if password1 and password2 and password1 != password2:
        #         raise ValidationError("Password didn't match")
        #     return password2

class CreateHealthProfile(ModelForm):
    class Meta:
        model = HealthProfile
        fields = ['healthConditions', 'height', 'weight']

class CreateAddress(ModelForm):
    class Meta:
        model = Address
        fields = ['houseNumber', 'kebele', 'subCity', 'regionOrCity', 'country']

class CreateAdmin(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['firstName', 'lastName', 'email', 'phoneNumber', 'username', 'password', 'profilePicture', 'creationDateTime']
        USERNAME_FIELD = 'username'

class CreateHealthFacilityAccount(ModelForm):
    class Meta:
        model = HealthFacilityAccount
        fields = ['healthFacilityOrAmbulanceID', 'healthFacilityType', 'username', 'email', 'password', 'creationDateTime', 'logo', 'additionalAttributes']
        USERNAME_FIELD = 'username'

class CreateHealthCareFacility(ModelForm):
    class Meta:
        model = HealthCareFacility
        fields = ['name', 'branch', 'description', 'address', 'averageRating', 'GPSCoordinates', 'verificationStatus', 'website', 'email', 'phoneNumber', 'source', 'imageGallery', 'tags', 'accountID', 'creationDateTime', 'type', 'services', 'capacity', 'doctorCount', 'averageNumberOfUsers', 'additionalAttributes']
        USERNAME_FIELD = 'email'

class CreateAppointment(ModelForm): #healthFacilityID is a foreignkey
    class Meta:
        model = Appointment
        fields = ['userID', 'healthFacilityID', 'healthFacilityType', 'dateTime', 'status']
    
class CreateUserRating(ModelForm): # userID and healthFacilityID are foreignkeys
    class Meta:
        model = UserRating
        fields = ['userID', 'healthFacilityID', 'rating', 'healthFacilityType', 'creationDateTime', 'lastUpdateTime']

class CreateUserReview(ModelForm): # foreignkey = userID, healthFacilityID
    class Meta:
        model = UserReview
        fields = ['userID', 'healthCareFacilityID', 'review', 'healthFacilityType', 'creationDateTime', 'lastUpdateTime']

class CreateReviewComment(ModelForm): #foreignkey = commenterID, UserReviewID
    class Meta:
        model = ReviewComment
        fields = ['commenterID', 'UserReviewID', 'comment', 'creationDateTime', 'lastUpdatetime']

class CreateAmbulanceService(ModelForm):
    class Meta:
        model = AmbulanceService
        fields = ['name', 'branch', 'description', 'address', 'averageRating', 'GPSCoordinates', 'verificationStatus', 'website', 'email', 'phoneNumber', 'source', 'imageGallery', 'tags', 'accountID', 'creationDateTime', 'additionalAttributes']

class CreateAmbulance(ModelForm): #foreignkey = healthFacilityID, accountID
    class Meta:
        model = Ambulance
        fields = ['healthFacilityID', 'healthFacilityType', 'driverFirstName', 'driverLastName', 'isAvailable', 'username', 'email', 'password', 'phoneNumber', 'accountID', 'additionalAttributes']

class CreateHealthCareService(ModelForm): # healthCareFacilityID foreignkey
    class Meta:
        model = HealthCareService
        fields = ['healthCareFacilityID', 'service', 'Row3']

class CreateClaimRequest(ModelForm): #foreignkey = healthFacilityID
    class Meta:
        model = ClaimRequest
        fields = ['healthFacilityID', 'requesterPhoneNumber', 'requesterFirstName', 'requesterLastName', 'requesterEmail', 'message', 'attachment', 'status', 'isDone', 'dateTime', 'cancelDateTime']

class CreateAutomations(ModelForm):
    class Meta:
        model = Automations
        fields = ['name', 'description', 'triggers', 'actions', 'isActive', 'creationDateTime', 'tags']

class CreateHeartRateHistory(ModelForm):
    class Meta:
        model = HeartRateHistory
        fields = ['dateTime', 'reading']

class CreateSleepHistory(ModelForm):
    class Meta:
        model = SleepHistory
        fields = ['date', 'hours']