# Generated by Django 4.0.6 on 2022-08-22 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0019_delete_database_delete_databasetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=20, unique=True)),
                ('slug', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=20)),
                ('host_ipaddress', models.CharField(max_length=20)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('port', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.CharField(blank=True, choices=[('Prod', 'Prod'), ('Test', 'Test'), ('Dev', 'Dev'), ('UAT', 'UAT')], max_length=20, null=True)),
                ('applications_hosted', models.CharField(blank=True, max_length=20, null=True)),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('support_group', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('database_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.databasetype')),
                ('hostname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.server')),
            ],
        ),
        migrations.AddIndex(
            model_name='database',
            index=models.Index(fields=['database_name'], name='Idx_databasename'),
        ),
        migrations.AddIndex(
            model_name='database',
            index=models.Index(fields=['status'], name='Idx_DatabaseStatus'),
        ),
    ]