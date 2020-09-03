# Generated by Django 3.1.1 on 2020-09-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200903_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='short_description',
        ),
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(max_length=250),
        ),
    ]