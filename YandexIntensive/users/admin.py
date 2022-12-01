from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile, User


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine, ]
