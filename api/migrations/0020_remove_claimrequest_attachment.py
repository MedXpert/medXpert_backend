# Generated by Django 4.0.4 on 2022-06-19 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_claimrequest_requesteraccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claimrequest',
            name='attachment',
        ),
    ]
