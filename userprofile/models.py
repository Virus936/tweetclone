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


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.follower} {self.following}"

    def __repr__(self):
        return f"{self.follower} {self.following}"

    class Meta:
        unique_together = ["follower", "following"]
