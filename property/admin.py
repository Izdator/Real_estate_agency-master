from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner'] #add search to admin UI.
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    list_editable = ('new_building',)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'created_at')
    raw_id_fields = ('flat',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

