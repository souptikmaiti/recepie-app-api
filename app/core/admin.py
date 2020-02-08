from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (  # Section 1 with no title
            None,
            {
                'fields': ('email', 'password')
            }
        ),
        (  # Section 2 with title Personal Info
            _('Personal Info'),
            {
                'fields': ('name',)
            }
        ),
        (  # Section 3 with title Permissions
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (  # Section 4 with title Important dates
            _('Important dates'),
            {
                'fields': ('last_login',)
            }
        )
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
