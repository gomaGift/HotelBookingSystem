from django.contrib import admin
from .models import User
from .forms import SignUpForm
from django.utils.translation import gettext_lazy as _


# Register your models here.

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = SignUpForm
    
    model = User
    list_display = ("username","email", "phone_number", "is_active","user_role",)
    list_filter = ("email", "user_role", "is_active",)
    fieldsets = (
        (None, {"fields": ( "password",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email","phone_number",'date_of_birth',"profile_pic")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        ("Role details", {"fields": ("user_role",)})

    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    search_fields = ("username", "first_name", "last_name", "email")
    

