# Generated by Django 4.0.6 on 2022-08-12 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_diskvolumes_free_space_pc_diskvolumes_used_space_pc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CpuUsageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('CpuUsage', models.SmallIntegerField(blank=True, null=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.server')),
            ],
        ),
    ]