# Generated by Django 4.2.10 on 2024-12-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0013_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Missing_Log',
            fields=[
                ('fleet', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_number', models.CharField(blank=True, max_length=255, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=255, null=True)),
                ('ownership', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('generate_series', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'missing_log',
                'managed': False,
            },
        ),
    ]
