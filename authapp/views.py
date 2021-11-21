
from django.contrib.auth import authenticate, get_user_model

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import Jurusan, User
from authapp.models import Student

from .permissions import (
    IsSelf,
)

from .serializers import (
    StudentSerializer,
    UserSerializer,
)

# Create your views here.
def user_data_default_permissions(action):
    if action == "list":
        permission_classes = [IsAuthenticated]
    
    return [permission() for permission in permission_classes]


# Default Response on List Action for User's Data
def user_data_list_action(request, queryset, serializer):
    queryset = queryset.filter(user=request.user.id)
    serializer = serializer(queryset, many=True)
    return Response(serializer.data)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        print("aha")
        if not bool(request.data.get("username", None)):
            return Response(
                data={"username": "This field is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not bool(request.data.get("password", None)):
            return Response(
                data={"password": "This field is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if get_user_model().objects.filter(username = request.data.get("username")).exists():
            user = get_user_model().objects.filter(username = request.data.get("username")).first()
        else :
            raise AuthenticationFailed("Username not found!")
        
        
        if not user.check_password(request.data.get("password")):
            raise AuthenticationFailed("Incorrect password!")
        
        def get_token(user):
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        
        response = Response()
        response.data = get_token(user)
        response.data.update({"message" : "success"})
        return response

class RegisterView(APIView):
    def post(self, request):
        if (
            request.data.get("username", None)
            and request.data.get("password", None)
            and request.data.get("email", None)
            and Jurusan.objects.filter(id=request.data.get("jurusan")).exists()
        ): 
            user = UserSerializer(data=request.data)
            if user.is_valid():
                user.save()
                request.data._mutable = True
                request.data.update({
                    "user" : user.data.get("id"),
                    })
                student = StudentSerializer(data=request.data)
                if student.is_valid():
                    student.save()
                    return Response(data=student.data, status=status.HTTP_200_OK)
        else:
            data = {
                "username": "This fields is required",
                "email": "This fields is required",
                "password": "This fields is required",
                "jurusan": "This fields is required and must be exists",
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "delete" or self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get_permissions(self):
        if self.action == "list" or self.action == "delete" or self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

