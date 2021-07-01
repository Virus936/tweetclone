from django.urls import path, include
from .views import TweetList, TweetDetail, LikeToggle
from rest_framework import routers
from .views import TweetViewSet

router = routers.SimpleRouter()
router.register("tweets", TweetViewSet)

urlpatterns = [
    # path("tweets/", TweetList.as_view()),
    # path("tweets/<int:pk>", TweetDetail.as_view()),
    path("like/<int:pk>", LikeToggle.as_view()),
    path("", include(router.urls)),
]
