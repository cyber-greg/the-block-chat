from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active')
    ordering = ['email']

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('is_active','is_staff',),
        }),
        ('Infos personnelles', {
            'classes': ('wide',),
            'fields': ('email', 'password', 'full_name', ),
        }),
        ('Permissions', {
            'classes': ('wide',),
            'fields': ('groups',),
        }),
    )
    readonly_fields = ('date_joined',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', ),
        }),
        (None, {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_active', 'date_joined', ),
        }),
        (None, {
            'classes': ('wide',),
            'fields': ('groups', ),
        }),
    )
    pass
