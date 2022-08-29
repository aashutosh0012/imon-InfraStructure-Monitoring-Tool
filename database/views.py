from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.db.models import Q
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.core import serializers
import plotly.express as px
import pandas
import time


from .models import *
from .forms import *

class DatabaseListView(ListView):
	context_object_name = 'database_list'
	template_name = 'templates/database_home.html'
	def get_queryset(self, *args, **kwargs): 
		query = self.request.GET.get('search', default="")
		database_list = Database.objects.filter( Q(database_name__icontains=query) | Q(database_name__icontains=query)).order_by('-id')
		database_list = serializers.serialize("python", database_list)   
		print(database_list)
		return database_list

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['database_fields'] = [ field.name for field in Database._meta.fields if (field.name not in ('id','slug'))]
		return context


class DatabaseSearchListView(ListView):
	context_object_name = 'database_list'
	template_name = 'templates/components/database_list.html'
	def get_queryset(self, *args, **kwargs): 
		query = self.request.GET.get('search', default="")
		database_list = Database.objects.filter( Q(database_name__icontains=query)).order_by('-id')
		database_list = serializers.serialize("python", database_list)   
		print(database_list)
		return database_list

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['database_fields'] = [ field.name for field in Database._meta.fields if (field.name not in ('id','slug'))]
		return context


class DatabaseAddView(CreateView):
    model = Database
    form_class = AddDatabaseForm
    template_name = 'templates/components/database_add_form.html'
    success_url = reverse_lazy('database-reload')
    # messages.success(self.request, "New server added." )
    def form_valid(self, form):
        return super().form_valid(form)


def DatabaseCancelView(request):
    print("\nView = cancel\n")
    template = 'templates/components/database_add_button.html'
    return render(request,template)


def DatabaseReload(request):
    template = 'templates/components/database_addbutton_list.html'
    query = request.GET.get('search', default="")
    database_list = Database.objects.filter( Q(database_name__icontains=query)).order_by('-id')
    database_list = serializers.serialize("python", database_list)      
    # context['servers_list'] = database_list
    context = {'database_list' : database_list }
    context['fields'] = [ field.name for field in Database._meta.fields if (field.name not in ('id','slug'))] 
    return render(request,template, context)


class DatabaseDetailView(UpdateView):
	model = Database
	form_class = AddDatabaseForm
	template_name = 'templates/database_details.html'
	success_url = reverse_lazy('database-reload')


class DatabaseDeleteView(DeleteView):
	model = Database
	success_url = reverse_lazy('database-reload')
	template_name = 'templates/components/database_delete.html'


# last = time.perf_counter()
# def timer(step=''):
#     '''step=name of step where it was called'''
#     global last
#     now=time.perf_counter()
#     print(f'{now-last:0.6f} - {step}')
#     last = now

# class ServerDetailView(UpdateView):
#     last = time.perf_counter()
#     model = Server
#     form_class = AddServerForm
#     template_name = 'templates/components/ServerDetail.html'
#     success_url = reverse_lazy('reload')
#     def get_context_data(self, **kwargs): 
#         context = super().get_context_data(**kwargs)
#         try:
#             # context['serverMetrics'] = get_object_or_404(ServerMetrics, server__server_name=self.kwargs['slug'])
#             context['serverMetrics'] = ServerMetrics.objects.get(server__server_name=self.kwargs['slug'])
#         except:
#             pass
#         try:
#             context['DiskVolumes'] = DiskVolumes.objects.filter(server__server_name=self.kwargs['slug'])
#         except:
#             pass
#         try:
#             diskPercentage = DiskVolumes.objects.filter(server__server_name=self.kwargs['slug']).values('name','used_space_pc','free_space_pc')
#             diskPercentage_df = pandas.DataFrame(diskPercentage)
#             diskPercentage_fig = px.bar(
#                 diskPercentage_df,
#                 x='name', 
#                 y=['used_space_pc','free_space_pc'], 
#                 title="Disk Usage",
#                 text_auto=True,
#                 labels={
#                          "name": "Disks",
#                          "value": "Usage & Free %",
#                      })
#             context['diskUsageChart'] =  diskPercentage_fig.to_html()
#         except:
#             pass

#         try:
#             cpu_memory_usage_history = CPUMemoryUsageHistory.objects.filter(server__server_name=self.kwargs['slug']).values('time','CpuUsage','used_memory_pc')
#             cpu_memory_usage_df = pandas.DataFrame(cpu_memory_usage_history)
#             df = pandas.DataFrame(cpu_memory_usage_df)
#             cpu_memory_usage_fig = px.line(
#                 cpu_memory_usage_df, 
#                 x='time', 
#                 y=['CpuUsage','used_memory_pc'],
#                 markers=True,
#                 labels={
#                          "name": "Disks",
#                          "value": "Usage %",
#                      },
#                 )
#             context['cpu_memory_usage_fig'] = cpu_memory_usage_fig.to_html()
#         except:
#             pass
#         return context    



