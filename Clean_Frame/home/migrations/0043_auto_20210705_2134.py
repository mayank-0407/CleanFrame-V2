# Generated by Django 3.1.13 on 2021-07-05 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20210704_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 21, 34, 22, 33029)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 21, 34, 22, 33029)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 21, 34, 22, 33029)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 21, 34, 22, 33029)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 21, 34, 22, 31039)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 21, 34, 22, 31039)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 21, 34, 22, 31039)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 21, 34, 22, 31039)),
        ),
    ]
