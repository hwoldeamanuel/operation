# Generated by Django 4.2.10 on 2024-12-02 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_country_fieldoffice_region_zone_woreda_profile_and_more'),
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet_Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_number', models.CharField(blank=True, max_length=255, null=True)),
                ('month_log', models.CharField(blank=True, max_length=255, null=True)),
                ('year_log', models.IntegerField(blank=True, null=True)),
                ('start_km', models.FloatField(blank=True, null=True)),
                ('day_in_use', models.IntegerField(blank=True, null=True)),
                ('day_idle', models.IntegerField(blank=True, null=True)),
                ('day_in_workshop', models.IntegerField(blank=True, null=True)),
                ('workshop_visit', models.IntegerField(blank=True, null=True)),
                ('field_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.fieldoffice')),
                ('fleet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_to', to='fleet.fleet')),
            ],
        ),
    ]
