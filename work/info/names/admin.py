from django.contrib import admin

from .models import Name


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ("title", "address","city","category")
    search_fields = ("title","category")



   