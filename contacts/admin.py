from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "is_active", "created", "not_activated")
    search_fields = ("name", "phone", "email")
    list_filter = ("is_active", "not_activated", "created")
    readonly_fields = ("created",)
