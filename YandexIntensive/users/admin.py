from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, UpdateUserForm
from .models import Profile, CustomUser


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UpdateUserForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                       'password1',
                       'password2',
                       'is_staff', 'is'
                                   '_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(CustomUser)
class UserAdmin(CustomUserAdmin):
    inlines = [ProfileInLine, ]
