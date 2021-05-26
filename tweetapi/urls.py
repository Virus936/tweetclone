from django.urls import path
from .views import TweetList, TweetDetail, LikeToggle

urlpatterns = [
    path("tweets/", TweetList.as_view()),
    path("tweets/<int:pk>", TweetDetail.as_view()),
    path("like/<int:pk>", LikeToggle.as_view()),
]
