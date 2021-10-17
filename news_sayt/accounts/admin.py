from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import forms, models


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser

    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
    )


admin.site.register(models.CustomUser, CustomUserAdmin)