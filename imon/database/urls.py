from django.urls import path, include
from database.views import *
urlpatterns = [
    path('', DatabaseListView.as_view(), name='database-home'),
    path('search/', DatabaseSearchListView.as_view(), name='database-search'),
    path('add/', DatabaseAddView.as_view(),name='database-add'),
    path('cancel/', DatabaseCancelView, name='database-cancel'),
    path('reload/', DatabaseReload, name='database-reload'),    
    path('<slug:slug>/', DatabaseDetailView.as_view(),name='database-detail'),
    # path('<slug:slug>/delete/', DeleteServerView.as_view(),name='delete-server'),
]
