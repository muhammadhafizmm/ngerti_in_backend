from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from authapp.models import Jurusan
from authapp.serializers import JurusanSerializer
from .serializers import (
    MapelSerializer,
    MateriSerializer, 
    SoalSerializer,
    HasilKuisSerializer
)
from .models import (
    Mapel,
    Modul,
    Materi,
    Soal,
    HasilKuis
) 

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
        self.data = data
        return Response(data)

class MateriController(viewsets.ModelViewSet):
    queryset = Materi.objects.all()
    serializer_class = MateriSerializer

    def retrieve(self, request, pk = None):
        materi = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(materi)
        data = {"materi_data": serializer.data}
        data["soal"] = [
            {
                "id": soal.id, 
                "pertanyaan": soal.pertanyaan,
                "jawaban": soal.jawaban,
                "jawaban_benar": soal.jawaban_benar
            } for soal in Soal.objects.filter(materi=materi.id)]
        return Response(data)

class SoalController(viewsets.ModelViewSet):
    queryset = Soal.objects.all()
    serializer_class = SoalSerializer

    def retrieve(self, request, pk = None):
        soal = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(soal)
        return Response(serializer.data)

class HasilKuisController(viewsets.ModelViewSet):
    queryset = HasilKuis.objects.all()
    serializer_class = HasilKuisSerializer

    def retrieve(self, request, pk = None):
        hasil = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(hasil)
        data = {"hasil_data": serializer.data}
        data['hasil_data']['jawaban'] = [soal.jawaban_benar for soal in Soal.objects.filter(materi=self.queryset[0].materi.id)]

        return Response(data)

    # def hitung_nilai(self, jawaban):
    #     answer = jawaban[0].answer
    #     return(jawaban[0].materi.soal)
    #     this_materi = Materi.objects.get(id = jawaban[0].materi.id)
    #     print(serializer.data)

