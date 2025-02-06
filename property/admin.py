from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner'] #add search to admin UI.
    readonly_fields = ('created_at',)

admin.site.register(Flat, FlatAdmin)

