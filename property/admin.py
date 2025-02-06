from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner'] #add search to admin UI.

admin.site.register(Flat, FlatAdmin)

