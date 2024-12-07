# Generated by Django 4.2.10 on 2024-12-06 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_country_fieldoffice_region_zone_woreda_profile_and_more'),
        ('fleet', '0006_fleet_log_km_driven'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet_Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_number', models.CharField(blank=True, max_length=255, null=True)),
                ('month_expense', models.CharField(blank=True, max_length=255, null=True)),
                ('year_expense', models.IntegerField(blank=True, null=True)),
                ('expense_type', models.CharField(blank=True, max_length=255, null=True)),
                ('expense_volume', models.FloatField(blank=True, null=True)),
                ('expense_value', models.FloatField(blank=True, null=True)),
                ('volume_unit', models.CharField(blank=True, max_length=255, null=True)),
                ('expense_start_date', models.DateField(blank=True, null=True)),
                ('field_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.fieldoffice')),
                ('fleet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assign_to', to='fleet.fleet')),
            ],
        ),
    ]
