# Generated by Django 2.2.14 on 2020-07-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('arrival_date', models.DateTimeField()),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('special_signs', models.TextField()),
            ],
        ),
    ]
