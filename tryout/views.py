from django.contrib.auth import authenticate, get_user_model

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.generics import get_object_or_404

import csv, time

from .serializers import (
    TryOutSerializer
)

from .models import (
    TryOut
)

class TryOutViewSet(viewsets.ModelViewSet):
    queryset = TryOut.objects.all()
    serializer_class = TryOutSerializer

    def retrieve(self, request, pk = None):
        tryout = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(tryout)
        all_data = serializer.data
        soal = all_data["file_soal"]
        csvFilePath = soal[1:4] + ".csv"
        data = []
        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for csvRow in csvReader:
                data.append(csvRow)

        response = Response()
        response.data = {"tryout_detail" : serializer.data,
        "soal" : data}

        return response

