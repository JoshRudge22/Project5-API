from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'full_name', 'created_at')
    search_fields = ('user__username', 'username', 'full_name')

