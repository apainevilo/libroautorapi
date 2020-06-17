from rest_framework import serializers
from .models import Autor,Libro


class autorserializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

class libroserializers(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = "__all__"





