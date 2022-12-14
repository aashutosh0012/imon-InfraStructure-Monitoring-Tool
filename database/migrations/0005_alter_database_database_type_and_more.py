# Generated by Django 4.0.6 on 2022-08-24 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_database_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='database_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.databasetype', to_field='database_type'),
        ),
        migrations.AlterField(
            model_name='databasetype',
            name='database_type',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
