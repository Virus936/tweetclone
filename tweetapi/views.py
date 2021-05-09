from rest_framework import generics
from tweetapi.models import Tweet
from tweetapi.serializer import TweetSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TweetList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Tweet.objects.all().order_by("-date_created")
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TweetDetail(generics.RetrieveDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
