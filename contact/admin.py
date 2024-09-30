from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
SITE_ID = 1  # This should match your site's ID in the Sites admin panel
