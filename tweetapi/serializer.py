from .models import Tweet
from rest_framework import serializers


class TweetSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Tweet
        fields = [
            "id",
            "author",
            "content",
        ]
