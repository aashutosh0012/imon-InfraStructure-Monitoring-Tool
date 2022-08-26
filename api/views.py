from inventory.models import Server
from database.models import Database
from api.serializers import ServerSerializer, DatabaseSerializer
from rest_framework import viewsets


class ServerViewSet(viewsets.ModelViewSet):
	queryset = Server.objects.all()
	serializer_class = ServerSerializer
	# template_name = 'templates/test.html'


class DatabaseViewSet(viewsets.ModelViewSet):
	queryset = Database.objects.all()
	serializer_class = DatabaseSerializer
	# template_name = 'templates/test.html'