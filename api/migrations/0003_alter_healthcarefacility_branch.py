# Generated by Django 4.0.4 on 2022-06-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_healthcarefacility_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcarefacility',
            name='branch',
            field=models.TextField(blank=True, null=True),
        ),
    ]