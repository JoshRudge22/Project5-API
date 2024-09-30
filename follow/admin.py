from django.contrib import admin
from .models import Follow

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
SITE_ID = 1  # This should match your site's ID in the Sites admin panel
