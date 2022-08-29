from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from inventory.models import *

class DatabaseType(models.Model):
	database_type = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.database_type


class Database(models.Model):
	database_name		= models.CharField(max_length=20, unique=True)
	status 				= models.CharField(max_length=20,null=True, blank=True, choices=[('UP','UP'),('Down','Down')])
	hostname 			= models.ForeignKey(Server,to_field='server_name', on_delete=models.CASCADE)
	database_type 		= models.ForeignKey(DatabaseType,to_field='database_type', on_delete=models.CASCADE,null=True, blank=True)
	version 			= models.CharField(max_length=20,null=True, blank=True)	
	port 				= models.CharField(max_length=20,null=True, blank=True)
	host_ipaddress		= models.GenericIPAddressField(protocol='IPv4', null=True,blank=True)	
	start_time 			= models.DateTimeField(null=True, blank=True)	
	role 				= models.CharField(max_length=20, choices=[('Prod','Prod'),('Test','Test'),('Dev','Dev'),('UAT','UAT')], null=True,blank=True)
	applications_hosted	= models.CharField(max_length=20, null=True,blank=True)
	owner 				= models.CharField(max_length=50, null=True,blank=True)
	support_group 		= models.CharField(max_length=50, null=True,blank=True)
	description 		= models.CharField(max_length=250, null=True,blank=True)
	slug 				= models.CharField(max_length=20,blank=True, null=True)

	class Meta:
		indexes = [
			models.Index(fields=['database_name',], name='Idx_databasename'),
			models.Index(fields=['status'], name='Idx_DatabaseStatus'),
		]  
		ordering = ['-id']  

	def __str__(self):
		return self.database_name

	def get_absolute_url(self):
		return reverse('database',kwargs={'slug' : self.slug})  

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.database_name)
		self.host_ipaddress = self.hostname.ip_address
		super().save(*args, **kwargs)


# class Server(models.Model):
# 	server_name = models.CharField(max_length=50, unique=True)
# 	slug		= models.SlugField(blank=True, null=True)
# 	hostname	= models.CharField(max_length=50, null=True, blank=True)
# 	ip_address	= models.GenericIPAddressField(protocol='both', unpack_ipv4=True, unique=True, null=True, blank=True)
# 	status		= models.CharField(max_length=20, null=True, blank=True, choices=[('Running','Running'),('Stopped','Stopped'),('Warning','Warning'),('Critical','Critical'),('Online','Online'),('Offline','Offline')])
# 	life 		= models.CharField(max_length=20, null=True, blank=True, choices=[('Active','Active'),('In Service','In Service'),('Decomissioned','Decomissioned'),('In Maintenance','In Maintenance'),('Repair','Repair'),('Provisioning','Provisioning')])
# 	ipv4 		= models.GenericIPAddressField(protocol='IPv4', null=True,blank=True, unique=True)
# 	ipv6 		= models.GenericIPAddressField(protocol='IPv6', null=True,blank=True, unique=True)
# 	server_role	= models.CharField(max_length=20, choices=[('Prod','Prod'),('Test','Test'),('Dev','Dev'),('UAT','UAT')], null=True,blank=True)
# 	host_type	= models.CharField(max_length=20, choices=[('Physical','Physical'),('Virtual','Virtual')], null=True,blank=True)
# 	domain		= models.CharField(max_length=50, null=True,blank=True)
# 	os			= models.CharField(max_length=20, null=True,blank=True)
# 	os_family	= models.CharField(null=True, blank=True,max_length=20, choices = [('Unix','Unix'),('Win','Windows')])
# 	applications_hosted	= models.CharField(max_length=20, null=True,blank=True)
# 	owner 		= models.CharField(max_length=50, null=True,blank=True)
# 	support_group 	= models.CharField(max_length=50, null=True,blank=True)
# 	region 		= models.CharField(max_length=10, null=True,blank=True)
# 	country 	= models.CharField(max_length=32, null=True,blank=True)
# 	site 		= models.CharField(max_length=10, null=True,blank=True)
# 	description = models.CharField(max_length=250, null=True,blank=True)

	# def calculations(self):
	# 	self.free_memory = self.total_memory - self.used_memory
	# 	self.free_memory_pc = (self.free_memory/self.total_memory)*100
	# 	self.used_memory_pc = 100-self.free_memory_pc

	# def save(self, *args, **kwargs):
	# 	self.calculations()
	# 	super().save(*args, **kwargs)
