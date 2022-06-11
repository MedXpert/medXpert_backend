# Generated by Django 4.0.4 on 2022-06-10 15:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcarefacility',
            name='GPSCoordinates',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='accountID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.healthfacilityaccount'),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='additionalAttributes',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.admin'),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='averageNumberOfUsers',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='averageRating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='branch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='capacity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='creationDateTime',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='doctorCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='imageGallery',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='services',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='source',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='tags',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='verificationStatus',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
