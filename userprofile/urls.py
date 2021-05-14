from django.urls import path
from userprofile.views import UserView, ProfileView, Profile

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="Profile"),
    path("test/", Profile, name="ProfileTest"),
    path("user/<int:pk>", UserView.as_view(), name="profil"),
]
