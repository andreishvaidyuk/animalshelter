# Generated by Django 2.2.14 on 2020-07-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0004_auto_20200711_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='arrival_date',
            field=models.DateTimeField(),
        ),
    ]
