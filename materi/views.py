from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .permissions import (
    IsJurusan, 
    IsMapelJurusan
)


from authapp.models import Jurusan
from authapp.serializers import JurusanSerializer
from .serializers import (
    MapelSerializer,
    MateriSerializer, 
    SoalSerializer
)
from .models import (
    Mapel,
    Modul,
    Materi,
    Soal
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
    
    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [IsMapelJurusan]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class MateriController(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        materi = Materi.objects.all()
        serializer = MateriSerializer(materi, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MateriSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        queryset = Materi.objects.all()
        materi = get_object_or_404(queryset, pk=pk)
        allsoal = Soal.objects.filter(materi__id=pk)
        print(allsoal)
        serializer = MateriSerializer(materi)
        test = serializer.data
        print(test)
        return Response(serializer.data)

    def update(self, request, pk = None):
        materi = Materi.objects.get(pk = pk)
        serializer = MateriSerializer(materi, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        materi = Materi.objects.get(pk = pk)
        materi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SoalController(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        soal = Soal.objects.all()
        serializer = SoalSerializer(soal, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SoalSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        queryset = Soal.objects.all()
        soal = get_object_or_404(queryset, pk=pk)
        serializer = SoalSerializer(soal)
        return Response(serializer.data)

    def update(self, request, pk = None):
        soal = Soal.objects.get(pk = pk)
        serializer = MateriSerializer(soal, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        soal = Soal.objects.get(pk = pk)
        soal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          
