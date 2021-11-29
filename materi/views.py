from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import (
    Materi, Soal 
)
from .serializers import (
    MateriSerializer, SoalSerializer
)


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
          