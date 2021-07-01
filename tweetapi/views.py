from rest_framework import generics, viewsets
from tweetapi.models import Tweet
from tweetapi.serializer import TweetSerializer, TweetLikeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


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


class TweetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Tweet.objects.all().order_by("-date_created")
    serializer_class = TweetSerializer
    ordering = ("-date_created",)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
