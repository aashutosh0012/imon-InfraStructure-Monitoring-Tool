from django.urls import path, include
from inventory.views import *
urlpatterns = [
    path('', ServerListView.as_view(), name='server'),
    path('search/', SearchListView.as_view(), name='search'),
    path('add/', AddServerView.as_view(),name='add-server'),
    path('cancel/', cancelView, name='cancel'),
    path('reload/', reload, name='reload'),    
    # path('<slug:slug>/', ServerDetailView.as_view(),name='server-detail'),
    path('<slug:slug>/', ServerDetailView.as_view(),name='server-detail-web'),
    path('<slug:slug>/delete/', DeleteServerView.as_view(),name='delete-server'),
]

