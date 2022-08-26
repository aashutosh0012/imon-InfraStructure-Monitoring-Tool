from rest_framework import serializers
from inventory.models import Server
from database.models import Database


class ServerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Server
		fields = '__all__'


class DatabaseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Database
		fields = '__all__'





