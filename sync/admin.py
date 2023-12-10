from django.contrib import admin
from sync.models import Items, UserOrder, Stock, StockOrder

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "item_name",
        "item_group",
        "item_number",
    )
    readonly_fields = [
        "created_at",
    ]


class UserOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "item",
    )
    readonly_fields = [
        "created_at",
    ]


class StockAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "item",
        "discontinued",
    )
    readonly_fields = [
        "created_at",
    ]


class StockOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "item",
        "admin",
    )
    readonly_fields = [
        "ordered_at",
    ]


admin.site.register(StockOrder, StockOrderAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(UserOrder, UserOrderAdmin)
admin.site.register(Items, ItemAdmin)
