from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from userprofile.serializers import UserSerializer, ProfileSerializer
from rest_framework import generics


class UserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_profile_serializer(*args, **kwargs):
        return ProfileSerializer(*args, **kwargs)

