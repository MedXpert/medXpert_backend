# Generated by Django 4.0.4 on 2022-06-11 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_appointment_healthfacilitytype_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='healthFacilityID',
            new_name='healthFacility',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='userID',
            new_name='user',
        ),
    ]
