# Generated by Django 4.0.6 on 2022-08-11 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_servermetrics_cpuusage_servermetrics_updated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servermetrics',
            old_name='CpuUsage',
            new_name='cpu_usage',
        ),
    ]
