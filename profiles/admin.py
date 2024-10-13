from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'full_name', 'created_at')
    search_fields = ('user__username', 'username', 'full_name')
<<<<<<< Updated upstream

=======
<<<<<<< HEAD
SITE_ID = 1  # This should match your site's ID in the Sites admin panel
=======

>>>>>>> cc7f036 (updated files)
>>>>>>> Stashed changes
