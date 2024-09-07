from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User


@admin.register(User)  # pola decorators
class UserAdmin(BaseUserAdmin):
    ordering = ['email',]
    list_display = ['email', 'nama', 'is_active', 'is_staff']

    fieldsets = (
        (None, {
            "fields": (
                ['email', 'password']
            ),
        }),
        ("Personal Info", {
            "fields": (
                ['nama', 'tmp_lahir', 'tgl_lahir', 'no_hp', 'img_user']
            ),
        }),
        ("Permissions", {
            "fields": (
                ['groups', 'is_active', 'is_staff', 'is_superuser']
            ),
        }),
    )

    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['nama', 'email', 'no_hp', 'password1', 'password2']
            }
        )
    ]


# admin.site.register(User, UserAdmin)
