from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("auteur du tweet", blank=True, null=True)
    picture = models.ImageField()
    date_created = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.author} : {self.content[30]}..."

    def __str__(self):
        return f"{self.author} : {self.content[30]}..."
