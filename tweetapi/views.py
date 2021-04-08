from rest_framework import generics
from tweetapi.models import Tweet
from tweetapi.serializer import TweetSerializer


class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TweetDetail(generics.RetrieveDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
