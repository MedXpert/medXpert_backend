# Generated by Django 4.0.4 on 2022-06-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220611_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
