# Generated by Django 4.0.4 on 2022-06-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_remove_user_createdby_remove_user_modifiedby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcarefacility',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]