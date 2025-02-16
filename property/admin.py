from django.contrib import admin
from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owners__name']
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
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'created_at')
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'get_owner_pure_phone')

    def get_owner_pure_phone(self, obj):
        return obj.get_owner_pure_phone()

    get_owner_pure_phone.short_description = 'Нормализованный номер владельца'


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
