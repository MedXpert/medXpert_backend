# Generated by Django 4.0.4 on 2022-06-11 04:10

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_healthcarefacility_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcarefacility',
            name='GPSCoordinates',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
