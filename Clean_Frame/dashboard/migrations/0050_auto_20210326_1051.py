# Generated by Django 2.2.19 on 2021-03-26 10:51

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0049_auto_20210325_1346'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileVisibilty',
            new_name='ProfileVisibility',
        ),
        migrations.AlterField(
            model_name='companyannouncement',
            name='announcement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 51, 16, 522596)),
        ),
        migrations.AlterField(
            model_name='companyannouncement',
            name='last_date_to_apply',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 51, 16, 522573)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 51, 16, 525764)),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 51, 16, 523852)),
        ),
    ]
