from django.contrib.auth import authenticate, get_user_model

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

import csv
import json

from .serializers import (
    TryOutSerializer
)

from .models import (
    TryOut
)

class TryOutViewSet(viewsets.ModelViewSet):
    queryset = TryOut.objects.all()
    serializer_class = TryOutSerializer

    def csv_to_json(csvFilePath, jsonFilePath):
        data = {}
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                key = rows['No']
                data[key] = rows
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
        
        csvFilePath = r'Names.csv'
        jsonFilePath = r'Names.json'
         

    def retrieve(self, request, pk = None):
        tryout = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(tryout)
        print(serializer.data)

