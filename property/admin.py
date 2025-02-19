from django.contrib import admin
from .models import Flat, Complaint, Owner

class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    extra = 1
    raw_id_fields = ('flat',)

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
    inlines = [OwnerInline]

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'created_at')
    raw_id_fields = ('flat',)
    list_filter = ('flat', 'user')  # Добавлено для фильтрации по новым related_name

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    inlines = [OwnerInline]  # Если хотите отображать квартиры владельца

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)