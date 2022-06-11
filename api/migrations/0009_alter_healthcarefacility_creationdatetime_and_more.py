# Generated by Django 4.0.4 on 2022-06-11 05:03

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220611_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcarefacility',
            name='creationDateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='imageGalleryLinks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='healthcarefacility',
            name='source_addedBy',
            field=models.CharField(choices=[('Scraper', 'Scraper'), ('User', 'User'), ('Admin', 'Admin')], default='Scraper', max_length=10),
        ),
    ]