# Generated by Django 3.1.1 on 2020-09-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200904_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
