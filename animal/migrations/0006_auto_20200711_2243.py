# Generated by Django 2.2.14 on 2020-07-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0005_auto_20200711_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='arrival_date',
            field=models.DateField(),
        ),
    ]
