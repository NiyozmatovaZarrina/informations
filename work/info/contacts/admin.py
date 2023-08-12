from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("phone","homephone","email","time","name" )
    search_fields = ("phone","time")



   