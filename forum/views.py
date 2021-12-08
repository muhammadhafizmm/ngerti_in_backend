from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import (
    IsOwner, 
    IsStudent
)

from .serializers import (
    PostSerializer
)
from .models import (
    Post
) 

# Create your views here.
# permission belom ya jangan lupa

class ForumViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_permissions(self):
    #     if self.action == "retrieve" or self.action == "create":
    #         permission_classes = [IsStudent]
    #     else:
    #         permission_classes = [IsOwner]
    #     return [permission() for permission in permission_classes]
