# Generated by Django 4.0.4 on 2022-06-18 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_remove_claimrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimrequest',
            name='requesterAccount',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]