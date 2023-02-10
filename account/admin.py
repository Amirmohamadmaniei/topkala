from account.models import User, OTP
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms_admin_panel import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone', 'email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('phone', 'email', 'password')}),
        ('personal', {'fields': ('f_name', 'l_name', 'birth_day')}),
        ('permission', {'fields': ('is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone', 'email', 'password1', 'password2')}),
        ('personal', {'fields': ('f_name', 'l_name', 'birth_day')}),
        ('permission', {'fields': ('is_admin', 'is_active')}),
    )

    search_fields = ('phone',)
    ordering = ('is_admin', 'created')
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(OTP)
