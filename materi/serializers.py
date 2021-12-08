from rest_framework import serializers
from .models import (
    HasilKuis,
    Mapel,
    Modul,
    Materi,
    Soal,
    HasilKuis
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

class SoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soal
        fields = '__all__'
        

class HasilKuisSerializer(serializers.ModelSerializer):
    class Meta:
        model = HasilKuis
        fields = '__all__'