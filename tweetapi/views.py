from rest_framework import generics, mixins, viewsets
from tweetapi.models import Tweet
from tweetapi.serializer import TweetSerializer, TweetLikeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from userprofile.permissions import IsOwnerOrReadOnly


class TweetList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Tweet.objects.all().order_by("-date_created")
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TweetDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class LikeToggle(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tweet.objects.all()
    serializer_class = TweetLikeSerializer


class TweetViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    # isOwner or read only for obj but
    # authenticated_users_only for post
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Tweet.objects.all().order_by("-date_created")
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
