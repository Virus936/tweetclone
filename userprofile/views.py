from django.contrib.auth.models import User
from rest_framework import status
from userprofile.serializers import UserSerializer
from rest_framework import generics
from userprofile.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsOwnerOrReadOnly,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


@api_view(["GET", "PUT"])
def Profile(request):
    user = request.user
    if request.method == "GET":
        serializer = UserSerializer(user, context={"request": request})
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsOwnerOrReadOnly,
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
