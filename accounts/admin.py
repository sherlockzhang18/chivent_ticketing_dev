from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering       = ("email",)
    list_display   = ("email", "username", "is_staff", "is_active")
    list_filter    = ("is_staff", "is_active", "is_superuser", "groups")
    
    search_fields  = ("email", "username")
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        (None, {
            "fields": ("email", "username", "password")
        }),
        ("Personal info", {
            "fields": ("first_name", "last_name")
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {
            "fields": ("last_login", "date_joined"),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_staff", "is_active"),
        }),
    )
