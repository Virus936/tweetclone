from .models import Tweet
from rest_framework import serializers
from userprofile.serializers import UserSerializer


class TweetSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ["id", "author", "picture", "content", "numlike"]


# Look a this link  to improve the author display
# https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
#
