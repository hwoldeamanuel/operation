# Generated by Django 4.2.10 on 2024-12-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_fleet_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet_log',
            name='end_km',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
