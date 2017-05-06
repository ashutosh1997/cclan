from django.contrib import admin
from user_account.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["post_text", "timestamp", "updated"]
    list_display_links = ["post_text", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["post_text"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
