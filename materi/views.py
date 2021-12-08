from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .permissions import (
    IsJurusan, 
    IsMapelJurusan
)

from authapp.serializers import JurusanSerializer
from .serializers import (
    MapelSerializer,
    MateriSerializer, 
    SoalSerializer,
    HasilKuisSerializer
)

from authapp.models import Jurusan
from .models import (
    Mapel,
    Modul,
    Materi,
    Soal,
    HasilKuis
) 
from forum.models import (Post)

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

    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [IsJurusan]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
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
                "modul": modul.name,
                "related_materi": [
                    {
                        "id": materi.id, 
                        "judul": materi.judul
                    } for materi in Materi.objects.filter(modul=modul.id)],
            } for modul in Modul.objects.filter(mapel=instance.id)]
        return Response(data)
    
    @action(detail=True, methods=["get"])
    def get_related_post (self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(instance=instance)
        data = {"mapel_data": serializer.data}
        data["related_post"] = [
            {
                "id": post.id, 
                "topik": post.topik, 
                "isi": post.isi, 
                "waktu": post.waktu,
                "pengirim": post.pengirim.username,
                "child_post_len": Post.objects.filter(Q(mata_pelajaran=instance.id) & Q(parent_post=post.id)).count()
            } for post in Post.objects.filter(Q(mata_pelajaran=instance.id) & Q(parent_post=None))]
        return Response(data)
    
    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [IsMapelJurusan]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

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
        real_ans = {}
        for soal in Soal.objects.filter(materi=self.queryset[0].materi.id):
            real_ans[soal.id] = soal.jawaban_benar

        score = self.hitung_nilai(data['hasil_data']['answer'], real_ans)

        data['hasil_data']['nilai'] = score
        
        return Response(data)

    def hitung_nilai(self, answer, real_ans):
        jumlah_soal = len(real_ans)
        jumlah_dijawab = len(answer)
        student_score = 0
        if(jumlah_soal!=0 or jumlah_dijawab!=0):
            for i in answer:
                if(answer[i]==real_ans[int(i)]):
                    student_score = student_score+1
            
            student_score = int((student_score/jumlah_soal)*100)

        return student_score

