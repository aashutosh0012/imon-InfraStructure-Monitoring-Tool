# Generated by Django 4.0.6 on 2022-08-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_diskvolumes_created_memoryusage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpuusage',
            name='CpuUsage',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servermetrics',
            name='load_average1',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servermetrics',
            name='load_average2',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servermetrics',
            name='load_average3',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servermetrics',
            name='uptime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diskvolumes',
            name='capacity',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diskvolumes',
            name='free_space',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='memoryusage',
            name='free',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='memoryusage',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servermetrics',
            name='cpu_cores',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
