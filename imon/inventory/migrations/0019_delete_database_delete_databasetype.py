# Generated by Django 4.0.6 on 2022-08-22 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_databasetype_database'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Database',
        ),
        migrations.DeleteModel(
            name='DatabaseType',
        ),
    ]
