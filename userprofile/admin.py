from django.contrib import admin
from userprofile.models import Profile, Follow


class ProfileAdmin(admin.ModelAdmin):
    pass


class FollowAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow, FollowAdmin)
