from django.contrib import admin
import phonenumbers

from .models import ClaimRequest, HealthCareFacility, User


class HealthCareFacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phoneNumbers', 'email')
    list_filter = ('name', 'address', 'phoneNumbers', 'email')
    search_fields = ('name', 'address', 'phoneNumbers', 'email')


class ClaimRequestAdmin(admin.ModelAdmin):
    list_display = ('requesterFirstName', 'requesterLastName',
                    'requesterEmail', 'requesterPhoneNumber', 'isDone')
    list_filter = ('requesterFirstName', 'requesterLastName',
                   'requesterEmail', 'requesterPhoneNumber', 'isDone')
    search_fields = ('requesterFirstName', 'requesterLastName',
                     'requesterEmail', 'requesterPhoneNumber', 'isDone')


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstName', 'lastName',
                    'sex', 'role', 'phoneNumber')
    list_filter = ('email', 'firstName', 'lastName',
                   'sex', 'role', 'phoneNumber')
    search_fields = ('email', 'firstName', 'lastName',
                     'sex', 'role', 'phoneNumber')

    exclude = ('user_permissions', 'groups', 'isDeleted', 'CreatedDate', 'isActive', 'Last login')

admin.site.site_header = "MedXPert Admin"
admin.site.site_title = "MedXpert Admin Portal"
admin.site.index_title = "Welcome to MedXpert Portal"

admin.site.register(User, UserAdmin)
admin.site.register(ClaimRequest, ClaimRequestAdmin)
admin.site.register(HealthCareFacility, HealthCareFacilityAdmin)
# Register your models here.
# admin.register(...model...)
