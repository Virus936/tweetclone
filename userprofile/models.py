from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.TextField(blank=True, null=True)
    pp = models.ImageField(
        default="profile_pics/default.png", upload_to="profile_pics/"
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
