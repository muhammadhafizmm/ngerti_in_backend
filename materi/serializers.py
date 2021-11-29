from django.db.models import fields
from rest_framework import serializers
from .models import (
    Materi, Soal
)

class MateriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materi
        fields = '__all__'

class SoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soal
        fields = '__all__'
        