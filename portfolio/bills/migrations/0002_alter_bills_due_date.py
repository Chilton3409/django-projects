# Generated by Django 4.0.5 on 2023-05-11 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 11, 0, 9, 58, 443686)),
        ),
    ]
