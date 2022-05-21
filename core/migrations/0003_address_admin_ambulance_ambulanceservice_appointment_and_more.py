# Generated by Django 4.0.3 on 2022-05-21 08:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_healthprofile_user_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseNumber', models.CharField(max_length=10)),
                ('kebele', models.IntegerField()),
                ('subCity', models.CharField(max_length=50)),
                ('regionOrCity', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('profilePicture', models.ImageField(upload_to='')),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthFacilityType', models.CharField(max_length=100)),
                ('driverFirstName', models.CharField(max_length=100)),
                ('driverLastName', models.CharField(max_length=100)),
                ('isAvailable', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('additionalAttributes', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='AmbulanceService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('averageRating', models.FloatField()),
                ('GPSCoordinates', models.CharField(max_length=100)),
                ('verificationStatus', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('source', models.CharField(max_length=100)),
                ('imageGallery', models.ImageField(upload_to='')),
                ('tags', models.CharField(max_length=100)),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('additionalAttributes', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthFacilityType', models.CharField(max_length=100)),
                ('dateTime', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Automations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('triggers', models.CharField(max_length=100)),
                ('actions', models.CharField(max_length=100)),
                ('isActive', models.CharField(max_length=100)),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClaimRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requesterPhoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('requesterFirstName', models.CharField(max_length=100)),
                ('requesterLastName', models.CharField(max_length=100)),
                ('requesterEmail', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('attachment', models.FileField(upload_to='')),
                ('status', models.CharField(max_length=50)),
                ('isDone', models.CharField(max_length=50)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('cancelDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HealthCareFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('descriptioni', models.CharField(max_length=500)),
                ('averageRating', models.FloatField()),
                ('GPSCoordinates', models.CharField(max_length=100)),
                ('verificationStatus', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('source', models.CharField(max_length=100)),
                ('imageGallery', models.ImageField(upload_to='')),
                ('tags', models.CharField(max_length=100)),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('type', models.CharField(max_length=100)),
                ('services', models.CharField(max_length=100)),
                ('capacity', models.CharField(max_length=100)),
                ('doctorCount', models.IntegerField()),
                ('averageNumberOfUsers', models.FloatField()),
                ('additionalAttributes', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='HealthCareService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('Row3', models.CharField(max_length=100)),
                ('HealthCareFacilityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthcarefacility')),
            ],
        ),
        migrations.CreateModel(
            name='HealthFacilityAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthFacilityType', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('logo', models.ImageField(upload_to='')),
                ('additionalAttributes', models.CharField(max_length=500)),
                ('healthFacilityOrAmbulanceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ambulanceservice')),
            ],
        ),
        migrations.CreateModel(
            name='HeartRateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('reading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('lastUpdateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='SleepHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('hours', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('healthFacilityType', models.CharField(max_length=100)),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('lastUpdateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('healthFacilityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthcarefacility')),
            ],
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('healthFacilityType', models.CharField(max_length=100)),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('lastUpdateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('healthFacilityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthcarefacility')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('profilePicture', models.ImageField(upload_to='')),
                ('creationDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('dateOfBirth', models.DateField()),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('additionalAttributes', models.CharField(max_length=500)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.address')),
                ('healthProfileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userreview',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users'),
        ),
        migrations.AddField(
            model_name='userrating',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users'),
        ),
        migrations.AddField(
            model_name='reviewcomment',
            name='UserReviewID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userreview'),
        ),
        migrations.AddField(
            model_name='reviewcomment',
            name='commenterID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userrating'),
        ),
        migrations.AddField(
            model_name='healthcarefacility',
            name='accountID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthfacilityaccount'),
        ),
        migrations.AddField(
            model_name='healthcarefacility',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.admin'),
        ),
        migrations.AddField(
            model_name='claimrequest',
            name='healthFacilityID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthcarefacility'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='healthFacilityID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthcarefacility'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users'),
        ),
        migrations.AddField(
            model_name='ambulanceservice',
            name='accountID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthcarefacility'),
        ),
        migrations.AddField(
            model_name='ambulanceservice',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.admin'),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='accountID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthfacilityaccount'),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='healthFacilityID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ambulanceservice'),
        ),
    ]
