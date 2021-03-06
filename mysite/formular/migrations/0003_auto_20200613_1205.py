# Generated by Django 3.0.7 on 2020-06-13 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formular', '0002_auto_20200613_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('ico', models.PositiveIntegerField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
