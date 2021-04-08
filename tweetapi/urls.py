from django.urls import path
from .views import TweetList

urlpatterns = [
    path("tweets/", TweetList.as_view()),
]
