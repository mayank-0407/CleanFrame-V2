# Generated by Django 2.2.19 on 2021-03-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_profilevisibilty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyannouncement',
            name='first_round',
            field=models.BooleanField(default=False),
        ),
    ]
