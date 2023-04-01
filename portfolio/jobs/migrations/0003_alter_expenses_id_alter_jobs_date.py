# Generated by Django 4.0.5 on 2023-03-30 14:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_income_jobs_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
