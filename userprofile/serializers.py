from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Follow


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["pp", "desc"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "profile"]

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile")
        profile_serializer = ProfileSerializer()
        super(self.__class__, self).update(instance, validated_data)
        super(ProfileSerializer, profile_serializer).update(
            instance.profile, profile_data
        )
        return instance


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["following"]
