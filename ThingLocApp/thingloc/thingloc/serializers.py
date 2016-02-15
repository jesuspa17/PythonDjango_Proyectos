# -*- coding: utf-8 -*-
from thingloc.thingloc.models import Categoria, Objeto

__author__ = 'jpallares'


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id','url', 'name')

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id','nombre_categoria',)

class ObjetoSerializer(serializers.HyperlinkedModelSerializer):

    category_name = serializers.SerializerMethodField()

    id_usuario = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.parent.name

    def get_user_id(self,obj):
        return obj.parent.username

    class Meta:
        model = Objeto
        # Añadimos los campos propios, los calculados, y un campo "oculto", que es el id.
        # Este campo lo genera automáticamente django, como clave primaria de cualquier objeto
        # Lo visualizamos, para que el usuario pueda utilizarlo en consultas GET, PUT y DELETE
        fields = ('id','nombre','recompensa','perdido','nombre_categoria','username','coordenadas','imagen')