from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from authapp import serializers

from authapp.models import Jurusan
from authapp.serializers import JurusanSerializer
import materi
from materi.serializers import MapelSerializer
from .models import Mapel, Modul, Materi

# Create your views here.
# permission belom ya jangan lupa
class JurusanViewSet(viewsets.ModelViewSet):
    queryset = Jurusan.objects.all()
    serializer_class = JurusanSerializer
    
    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(instance=instance)
        data = {"jurusan_data": serializer.data}
        data["related_mapel"] = [{"id": mapel.id, "mapel": mapel.name} for mapel in Mapel.objects.filter(jurusan=instance.id)]
        return Response(data)
    
class MapelViewSet(viewsets.ModelViewSet):
    queryset = Mapel.objects.all()
    serializer_class = MapelSerializer
    
    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(instance=instance)
        data = {"mapel_data": serializer.data}
        data["related_modul"] = [
            {
                "id": modul.id, 
                "mapel": modul.name,
                "related_materi": [
                    {
                        "id": materi.id, 
                        "judul": materi.judul
                    } for materi in Materi.objects.filter(modul=modul.id)],
            } for modul in Modul.objects.filter(mapel=instance.id)]
        return Response(data)