from rest_framework import serializers
from .models import (
    TryOut
)

class TryOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryOut
        fields = '__all__'