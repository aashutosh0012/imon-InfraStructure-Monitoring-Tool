from django.contrib import admin

# Register your models here.

from database.models import *
admin.site.register(Database)
admin.site.register(DatabaseType)