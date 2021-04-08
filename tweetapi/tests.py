from django.test import TestCase
from .models import Tweet, Like
from django.contrib.auth import get_user_model

User = get_user_model()


class LikeTest(TestCase):
    def test_if_a_like_work(self):
        user1 = User.objects.create(username="vira")
        tweet1 = Tweet.objects.create(author=user1, content="here is my first tweet")
        Like.objects.create(user=user1, tweet=tweet1)
        self.assertEqual(user1, tweet1.likes.first())

    def test_if_two_likes_work(self):
        user1 = User.objects.create(username="vira")
        user2 = User.objects.create(username="jule")
        tweet1 = Tweet.objects.create(author=user1, content="here is my first tweet")
        Like.objects.create(user=user1, tweet=tweet1)
        Like.objects.create(user=user2, tweet=tweet1)
        self.assertEqual(len(tweet1.likes.all()), 2)

    def test_the_list_of_users_likes(self):
        user1 = User.objects.create(username="vira")
        user2 = User.objects.create(username="Jule")
        tweet1 = Tweet.objects.create(author=user1, content="here is my first tweet")
        tweet2 = Tweet.objects.create(author=user1, content="here is my second tweet")
        Like.objects.create(user=user2, tweet=tweet1)
        Like.objects.create(user=user2, tweet=tweet2)
        self.assertEqual(len(user2.like_set.all()), 2)


class CreateTest(TestCase):
    def test_the_list_of_users_create(self):
        user1 = User.objects.create(username="vira")
        Tweet.objects.create(author=user1, content="here is my first tweet")
        Tweet.objects.create(author=user1, content="here is my second tweet")
        self.assertEqual(len(user1.tweet_set.all()), 2)
