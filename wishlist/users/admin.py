from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'email', 'identifier', 'name'
    search_fields = 'email', 'identifier', 'name'
    readonly_fields = 'identifier',
