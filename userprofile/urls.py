from django.urls import path
from userprofile.views import UserView

urlpatterns = [
    path("<int:pk>", UserView.as_view(), name="profil"),
]
