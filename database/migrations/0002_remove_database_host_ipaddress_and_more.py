# Generated by Django 4.0.6 on 2022-08-22 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_delete_database_delete_databasetype'),
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='database',
            name='host_ipaddress',
        ),
        migrations.AddField(
            model_name='database',
            name='host_ipaddress2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_ip', to='inventory.server', to_field='ip_address'),
        ),
    ]
