# Generated by Django 4.2.10 on 2024-12-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0003_fleet_log_end_km'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet_log',
            name='log_sheet',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
