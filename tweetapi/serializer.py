from .models import Tweet
from rest_framework import serializers
from userprofile.serializers import UserSerializer


class TweetSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likeornot = serializers.SerializerMethodField()

    def get_likeornot(self, obj):
        current_user = self.context["request"].user
        return (not current_user.is_authenticated) or current_user in obj.likes.all()

    class Meta:
        model = Tweet
        fields = [
            "id",
            "author",
            "picture",
            "content",
            "numlike",
            "likeornot",
            "date_created",
        ]


# Look a this link  to improve the author display
# https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers


class TweetLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["likes"]

    def update(self, obj, validated_data):
        current_user = self.context["request"].user
        if current_user in obj.likes.all():
            obj.likes.remove(current_user)
        else:
            obj.likes.add(current_user)
        return obj
