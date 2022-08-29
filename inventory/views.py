from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from inventory.models import Server, ServerMetrics
from inventory.models import *
from django.db.models import Q
from inventory.forms import AddServerForm
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.core import serializers
import plotly.express as px
import pandas
import time



#4 ServerListView
class ServerListView(ListView):
    context_object_name = 'servers_list'
    template_name = 'templates/ServerHome.html'    
    def get_queryset(self): 
        query = self.request.GET.get('search', default="")
        servers_list = Server.objects.filter( Q(server_name__icontains=query) | Q(ip_address__icontains=query)).order_by('-id')
        servers_list = serializers.serialize("python", servers_list)        
        return servers_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['fields'] = [ field.name for field in Server._meta.get_fields() if (field.name not in ('id','slug','servermetrics','diskvolumes','cpumemoryusagehistory','database','host_ip'))]
        context['fields'] = [ field.name for field in Server._meta.fields if (field.name not in ('id','slug'))]
        return context

#2 SearchListView
class SearchListView(ListView):
    # template_name = 'templates/components/servers_list.html'
    template_name = 'templates/components/servers_list.html'
    context_object_name = 'servers_list'
    def get_queryset(self): 
        query = self.request.GET.get('search', default="")
        servers_list = Server.objects.filter( Q(server_name__icontains=query) | Q(ip_address__icontains=query)).order_by('-id')
        servers_list = serializers.serialize("python", servers_list)        
        return servers_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['fields'] = [ field.name for field in Server._meta.get_fields() if (field.name not in ('id','slug','servermetrics','diskvolumes','cpumemoryusagehistory','database','host_ip'))]
        context['fields'] = [ field.name for field in Server._meta.fields if (field.name not in ('id','slug'))]
        return context


class AddServerView(CreateView):
    model = Server
    form_class = AddServerForm
    template_name = 'templates/components/AddServerForm.html'
    success_url = reverse_lazy('reload')
    # messages.success(self.request, "New server added." )
    def form_valid(self, form):
        return super().form_valid(form)


def cancelView(request):
    print("\nView = cancel\n")
    template = 'templates/components/addServerButton.html'
    return render(request,template)

last = time.perf_counter()
def timer(step=''):
    '''step=name of step where it was called'''
    global last
    now=time.perf_counter()
    print(f'{now-last:0.6f} - {step}')
    last = now

class ServerDetailView(UpdateView):
    last = time.perf_counter()
    model = Server
    form_class = AddServerForm
    template_name = 'templates/components/ServerDetail.html'
    success_url = reverse_lazy('reload')
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        try:
            # context['serverMetrics'] = get_object_or_404(ServerMetrics, server__server_name=self.kwargs['slug'])
            context['serverMetrics'] = ServerMetrics.objects.get(server__server_name=self.kwargs['slug'])
        except:
            pass
        try:
            context['DiskVolumes'] = DiskVolumes.objects.filter(server__server_name=self.kwargs['slug'])
        except:
            pass
        try:
            diskPercentage = DiskVolumes.objects.filter(server__server_name=self.kwargs['slug']).values('name','used_space_pc','free_space_pc')
            diskPercentage_df = pandas.DataFrame(diskPercentage)
            diskPercentage_fig = px.bar(
                diskPercentage_df,
                x='name', 
                y=['used_space_pc','free_space_pc'], 
                title="Disk Usage",
                text_auto=True,
                labels={
                         "name": "Disks",
                         "value": "Usage & Free %",
                     },
                color_discrete_map={
                    'used_space_pc': 'blue',
                    'free_space_pc': 'green'
                    }
                )
            # diskPercentage_fig.update_traces(marker_color='green')
            context['diskUsageChart'] =  diskPercentage_fig.to_html()
        except:
            pass

        try:
            cpu_memory_usage_history = CPUMemoryUsageHistory.objects.filter(server__server_name=self.kwargs['slug']).values('time','CpuUsage','used_memory_pc')
            cpu_memory_usage_df = pandas.DataFrame(cpu_memory_usage_history)
            df = pandas.DataFrame(cpu_memory_usage_df)
            cpu_memory_usage_fig = px.line(
                cpu_memory_usage_df, 
                x='time', 
                y=['CpuUsage','used_memory_pc'],
                markers=True,
                labels={
                         "name": "Disks",
                         "value": "Usage %",
                     },
                )
            context['cpu_memory_usage_fig'] = cpu_memory_usage_fig.to_html()
        except:
            pass
        return context    



def reload(request):
    template = 'templates/components/server_home.html'
    query = request.GET.get('search', default="")
    servers_list = Server.objects.filter( Q(server_name__icontains=query) | Q(ip_address__icontains=query)).order_by('-id')
    servers_list = serializers.serialize("python", servers_list)      
    # context['servers_list'] = servers_list
    context = {'servers_list' : servers_list }
    context['fields'] = [ field.name for field in Server._meta.fields if (field.name not in ('id','slug'))] 
    return render(request,template, context)


class DeleteServerView(DeleteView):
    model = Server
    success_url = reverse_lazy('reload')
    template_name = 'templates/components/DeleteServer.html'


class ServerMetricView(DetailView):
    model = ServerMetrics
    template_name = 'templates/components/server_Metric.html'










