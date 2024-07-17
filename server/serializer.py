from rest_framework import serializers  # Importamos el módulo de serializadores de Django REST.
from django.contrib.auth.models import User  # Importamos el modelo User de Django.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Asociamos este serializador al modelo User.
        fields = ['id', 'username', 'email', 'password']
        # Lista de campos que se incluirán en la respuesta serializada.

