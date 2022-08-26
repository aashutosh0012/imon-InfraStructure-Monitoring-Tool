from django.contrib import admin

#Register Inventory app Models (Server) in Admin view 
from inventory.models import *
#admin.site.register(Server)


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
	#list_display = ('server_name','hostname','ip_address','owner','os_family','os')
	# list_display = [ field.name for field in Server._meta.get_fields() if field.name != 'id' ]
	# list_display = [ field.name for field in Server._meta.get_fields() if (field.name not in ('id','slug')) ][4:] #
	# list_display = [ field.name for field in Server._meta.get_fields() if (field.name not in ('id','servermetrics','diskvolumes','cpumemoryusagehistory','database','host_ip')) ]
	list_display = [ field.name for field in Server._meta.fields if (field.name not in ('id')) ]
	list_filter = ('status','server_role','host_type','os_family','os')
	fieldsets = [
		('Primary Info',{
			# 'fields': [ field.name for field in Server._meta.get_fields() if (not field.null and field.name != 'id')],
			# 'fields': [ field.name for field in Server._meta.get_fields() if (not field.null and field.name not in ('id','servermetrics','diskvolumes','cpumemoryusagehistory','database','host_ip')) ],
			'fields': [ field.name for field in Server._meta.fields if (not field.null and field.name not in ('id')) ],
			}

		),
		('Other Info',{
			# 'fields':  [ field.name for field in Server._meta.get_fields() if (field.null and field.name not in ('id','servermetrics','diskvolumes','cpumemoryusagehistory','database','host_ip'))]
			'fields':  [ field.name for field in Server._meta.fields if (field.null and field.name not in ('id'))]
			}
		),

	]


admin.site.register(ServerMetrics)
admin.site.register(DiskVolumes)
admin.site.register(CPUMemoryUsageHistory)