# Generated by Django 4.2.10 on 2024-12-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0014_missing_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Missing_Expense',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_number', models.CharField(blank=True, max_length=255, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=255, null=True)),
                ('ownership', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('generate_series', models.DateField(blank=True, null=True)),
                ('expense_start_date', models.DateField(blank=True, null=True)),
                ('Fuel_cost', models.CharField(blank=True, max_length=255, null=True)),
                ('Cost_spares', models.CharField(blank=True, max_length=255, null=True)),
                ('Cost_labour', models.CharField(blank=True, max_length=255, null=True)),
                ('Cost_consumables', models.CharField(blank=True, max_length=255, null=True)),
                ('Rental_and_Tax', models.CharField(blank=True, max_length=255, null=True)),
                ('Rental_fees', models.CharField(blank=True, max_length=255, null=True)),
                ('Tax_Insurance', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'missing_expense',
                'managed': False,
            },
        ),
    ]
