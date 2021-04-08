from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    content = models.TextField("auteur du tweet", blank=True, null=True)
    picture = models.ImageField()
    date_created = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, through="Like")

    def __repr__(self):
        return f"{self.author} : {self.content}..."

    def __str__(self):
        return f"{self.author} : {self.content}..."


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="liked")
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["user", "tweet"]
