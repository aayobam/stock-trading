from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_superuser')
    readonly_fields = ("id",)
    ordering = ('email',)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
    )
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
    )