from rest_framework import serializers
from .models import (
    Mapel,
    Modul,
    Materi
)

class MateriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materi
        fields = '__all__'


class MapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapel
        fields = '__all__'

class ModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modul
        fields = '__all__'