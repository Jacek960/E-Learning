# Generated by Django 3.1.1 on 2020-09-04 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_order_premium_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.premium'),
        ),
    ]
