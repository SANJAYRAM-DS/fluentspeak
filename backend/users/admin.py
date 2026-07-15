from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    ordering = ("email",)

    list_display = (
        "email",
        "is_verified",
        "is_active",
        "is_staff",
        "created_at",
    )

    list_filter = (
        "is_active",
        "is_verified",
        "is_staff",
    )

    search_fields = (
        "email",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "last_login",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_verified",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "english_level",
        "native_language",
        "target_language",
        "daily_goal_minutes",
    )

    search_fields = (
        "user__email",
        "first_name",
        "last_name",
    )

    list_filter = (
        "english_level",
        "target_language",
    )