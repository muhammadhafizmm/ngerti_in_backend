
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers

from materi.models import Mapel
from .models import (
    Jurusan, 
    Student, 
    User,
)

# serializers_util
def get_empty_string_if_none(query):
    return query if query is not None else ""


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    no_hp = serializers.CharField(required=False) 
    
    def create(self, validated_data):
        try:
            user = get_user_model().objects.create_user(
                first_name=get_empty_string_if_none(validated_data.get("first_name", None)),
                last_name=get_empty_string_if_none(validated_data.get("last_name", None)),
                username=validated_data.get("username"),
                email=validated_data.get("email"),
                password=validated_data.get("password"),
                no_hp=get_empty_string_if_none(validated_data.get("no_hp", None)),
            )
            return user
        except:
            detail = {"detail": "Username or Email already taken"}
            raise serializers.ValidationError(detail=detail, code=400)

    def update(self, instance, validated_data):
        validated_data.pop("username", None)
        validated_data.pop("email", None)
        if validated_data.get("password", None):
            instance.set_password(validated_data.get("password"))
            instance.save()
            validated_data.pop("password")
        return super().update(instance, validated_data)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "no_hp",
        ]

class StudentSerializer(serializers.ModelSerializer):
    # write only
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
    )
    jurusan = serializers.PrimaryKeyRelatedField(
        queryset=Jurusan.objects.all(),
        write_only=True
    )
    
    # read only
    user_data = serializers.SerializerMethodField()
    jurusan_data = serializers.SerializerMethodField()
    
    # read_and_write
    is_premium = serializers.BooleanField(required=False)
    
    def create(self, validated_data):
        try:
            student = Student.objects.create(
                user=validated_data.get("user"),
                jurusan=validated_data.get("jurusan"),
                is_premium=validated_data.get("is_premium"),
            )
            return student
        except:
            detail = {"detail": "user already student"}
            raise serializers.ValidationError(detail=detail, code=400)
    
    def get_user_data(self, obj):
        return {
            "id" : obj.user.id,
            "username" : obj.user.username,
        }
        
    def get_jurusan_data(self, obj):
        return {
            "id" : obj.jurusan.id,
            "username" : obj.jurusan.name,
        }
    
    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "jurusan",
            "user_data",
            "jurusan_data",
            "is_premium"
        ]

class JurusanSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)

    class Meta:
        model = Jurusan
        fields = '__all__'