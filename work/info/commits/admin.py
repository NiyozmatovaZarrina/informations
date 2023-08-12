from django.contrib import admin

from .models import Commit


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title",)



   