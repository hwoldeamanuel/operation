# Generated by Django 4.2.10 on 2024-12-13 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0016_missed_expense'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='missed_expense',
            table='expenses',
        ),
    ]