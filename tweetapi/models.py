from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("contenu du tweet", blank=True, null=True)
    picture = models.ImageField(upload_to="tweet-images/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, through="Like", related_name="like_set", blank=True
    )

    def __repr__(self):
        return f"{self.author} : {self.content}..."

    def __str__(self):
        return f"{self.author} : {self.content}..."

    @property
    def numlike(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="liked")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "tweet"]
