# Generated by Django 4.0.5 on 2023-05-22 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0006_alter_bills_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 16, 35, 32, 8346)),
        ),
    ]
