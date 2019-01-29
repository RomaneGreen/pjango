from django.contrib import admin
from .models import UserProfile,TokenTransfer



admin.site.register(UserProfile)

admin.site.register(TokenTransfer)