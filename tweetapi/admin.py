from django.contrib import admin
from tweetapi.models import Tweet, Like

# Register your models here.
class LikeAdmin(admin.ModelAdmin):
    pass


class LikeTabularInline(admin.TabularInline):
    model = Like


class TweetAdmin(admin.ModelAdmin):
    inlines = [LikeTabularInline]

    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Like, LikeAdmin)
