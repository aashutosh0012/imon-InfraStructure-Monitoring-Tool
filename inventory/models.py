from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Server(models.Model):
	server_name = models.CharField(max_length=50, unique=True)
	slug		= models.SlugField(blank=True, null=True)
	hostname	= models.CharField(max_length=50, null=True, blank=True)
	ip_address	= models.GenericIPAddressField(protocol='both', unpack_ipv4=True, unique=True, null=True, blank=True)
	status		= models.CharField(max_length=20, null=True, blank=True, choices=[('Running','Running'),('Stopped','Stopped'),('Warning','Warning'),('Critical','Critical'),('Online','Online'),('Offline','Offline')])
	life 		= models.CharField(max_length=20, null=True, blank=True, choices=[('Active','Active'),('In Service','In Service'),('Decomissioned','Decomissioned'),('In Maintenance','In Maintenance'),('Repair','Repair'),('Provisioning','Provisioning')])
	ipv4 		= models.GenericIPAddressField(protocol='IPv4', null=True,blank=True, unique=True)
	ipv6 		= models.GenericIPAddressField(protocol='IPv6', null=True,blank=True, unique=True)
	server_role	= models.CharField(max_length=20, choices=[('Prod','Prod'),('Test','Test'),('Dev','Dev'),('UAT','UAT')], null=True,blank=True)
	host_type	= models.CharField(max_length=20, choices=[('Physical','Physical'),('Virtual','Virtual')], null=True,blank=True)
	domain		= models.CharField(max_length=50, null=True,blank=True)
	os			= models.CharField(max_length=20, null=True,blank=True)
	os_family	= models.CharField(null=True, blank=True,max_length=20, choices = [('Unix','Unix'),('Win','Windows')])
	applications_hosted	= models.CharField(max_length=20, null=True,blank=True)
	owner 		= models.CharField(max_length=50, null=True,blank=True)
	support_group 	= models.CharField(max_length=50, null=True,blank=True)
	region 		= models.CharField(max_length=10, null=True,blank=True)
	country 	= models.CharField(max_length=32, null=True,blank=True)
	site 		= models.CharField(max_length=10, null=True,blank=True)
	description = models.CharField(max_length=250, null=True,blank=True)

	class Meta:
		indexes = [
			models.Index(fields=['server_name','hostname','ip_address'], name='Idx_ServerHostname'),
			models.Index(fields=['status','life'], name='Idx_ServerStatus'),
		]    

	def __str__(self):
		return self.server_name

	# def get_absolute_url(self):
	# 	return reverse('server',kwargs={'pk' : self.pk})  

	def get_absolute_url(self):
		return reverse('server',kwargs={'slug' : self.slug})  

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.server_name)
		super().save(*args, **kwargs)




class ServerMetrics(models.Model):
	server = models.ForeignKey(Server, on_delete=models.CASCADE)
	status = models.CharField(max_length=10, choices=(('ONLINE','Online'),('OFFLINE','Offline')), default='ONLINE')
	cpu_cores = models.SmallIntegerField(null=True,blank=True)
	cpu_usage = models.SmallIntegerField(null=True,blank=True)
	total_memory = models.IntegerField(null=True,blank=True)
	free_memory = models.IntegerField(null=True,blank=True)
	used_memory = models.IntegerField(null=True,blank=True)
	free_memory_pc = models.PositiveBigIntegerField(default=0,null=True,blank=True)
	used_memory_pc = models.PositiveBigIntegerField(default=0,null=True,blank=True)
	swap_total = models.IntegerField(null=True,blank=True)
	swap_free = models.IntegerField(null=True,blank=True)
	swap_used = models.IntegerField(null=True,blank=True)
	uptime = models.DateTimeField(null=True,blank=True)
	load_average1 = models.SmallIntegerField(null=True,blank=True)
	load_average2 = models.SmallIntegerField(null=True,blank=True)
	load_average3 = models.SmallIntegerField(null=True,blank=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.server.server_name

	def percentage_calculations(self):
		self.free_memory_pc = (self.free_memory/self.total_memory)*100
		self.used_memory_pc = 100-self.free_memory_pc

	def save(self, *args, **kwargs):
		self.percentage_calculations()
		super().save(*args, **kwargs)

# class CpuUsageHistory(models.Model):
# 	server = models.ForeignKey(Server, on_delete=models.CASCADE)
# 	time = models.DateTimeField(auto_now=True)
# 	CpuUsage = models.SmallIntegerField(null=True,blank=True)

# 	def __str__(self):
# 		return self.server.server_name + ' ' + self.time.strftime("%d%b%Y-%H%M%S")

class CPUMemoryUsageHistory(models.Model):
	server = models.ForeignKey(Server, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now=True)
	CpuUsage = models.SmallIntegerField(default=0, null=True,blank=True)
	total_memory = models.IntegerField(null=True,blank=True)
	used_memory = models.IntegerField(null=True,blank=True)
	free_memory = models.IntegerField(null=True,blank=True)
	used_memory_pc = models.PositiveBigIntegerField(default=0,null=True,blank=True)
	free_memory_pc = models.PositiveBigIntegerField(default=0,null=True,blank=True)	
	swap_total = models.IntegerField(null=True,blank=True)
	swap_used = models.IntegerField(null=True,blank=True)
	swap_free = models.IntegerField(null=True,blank=True)
	
	def calculations(self):
		self.free_memory = self.total_memory - self.used_memory
		self.free_memory_pc = (self.free_memory/self.total_memory)*100
		self.used_memory_pc = 100-self.free_memory_pc

	def save(self, *args, **kwargs):
		self.calculations()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.server.server_name + ' ' + self.time.strftime("%d%b%Y-%H%M%S")




class DiskVolumes(models.Model):
	server = models.ForeignKey(Server, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	# created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	total_size = models.PositiveBigIntegerField(null=True,blank=True)
	used_space = models.PositiveBigIntegerField(null=True,blank=True)
	free_space = models.PositiveBigIntegerField(null=True,blank=True)
	free_space_pc = models.PositiveBigIntegerField(default=0,null=True,blank=True)
	used_space_pc = models.PositiveBigIntegerField(default=0,null=True,blank=True)

	def __str__(self):
		return self.name + ' ' + self.server.server_name

	def percentage_calculations(self):
		self.free_space_pc = (self.free_space/self.total_size)*100
		self.used_space_pc = 100-self.free_space_pc

	def save(self, *args, **kwargs):
		self.percentage_calculations()
		super().save(*args, **kwargs)



