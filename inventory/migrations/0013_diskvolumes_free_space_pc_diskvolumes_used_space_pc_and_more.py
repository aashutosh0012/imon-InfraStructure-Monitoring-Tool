# Generated by Django 4.0.6 on 2022-08-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_rename_capacity_diskvolumes_total_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diskvolumes',
            name='free_space_pc',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='diskvolumes',
            name='used_space_pc',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='servermetrics',
            name='free_memory_pc',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='servermetrics',
            name='used_memory_pc',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
    ]