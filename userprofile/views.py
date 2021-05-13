from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from userprofile.serializers import UserSerializer
from rest_framework import generics


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
