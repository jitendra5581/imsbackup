from django.contrib import admin
from .models import *

# Register your models here.


admin.site.site_header = 'IMS Dashboard'
admin.site.register(Measure)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_category', 'inventory_description', 'measure_Unit')



admin.site.register(Inventory,InventoryAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 
    'inventory_category', 
    'frontend_measure',
    'frontend_quantity',
    'purchase_price',
    'backend_measure',
    'backend_quantity'
    )


admin.site.register(Purchase,PurchaseAdmin)
