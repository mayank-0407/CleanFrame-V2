# Generated by Django 2.2.19 on 2021-03-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_studentregistration_internship_cleared'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpermissions',
            name='can_ban_users',
            field=models.BooleanField(default=False),
        ),
    ]
