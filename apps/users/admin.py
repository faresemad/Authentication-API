from django.contrib import admin

from apps.users.models import ActivationCode, CustomUserProfile


@admin.register(CustomUserProfile)
class CustomUserProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "first_name", "last_name", "date_joined", "is_active", "is_staff"]
    search_fields = ["email", "username", "first_name", "last_name"]
    list_filter = ["is_active", "is_staff"]

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "email_comfirmed", "email_verification_code")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )


admin.site.register(ActivationCode)
