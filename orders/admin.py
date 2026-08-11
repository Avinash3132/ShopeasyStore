from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'price', 'quantity', 'get_total_price']

    def get_total_price(self, obj):
        return f'${obj.get_total_price()}'
    get_total_price.short_description = 'Total'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'get_full_name', 'email', 'status',
        'total_price', 'created_at'
    ]
    list_filter = ['status', 'created_at']
    list_editable = ['status']
    search_fields = ['first_name', 'last_name', 'email']
    readonly_fields = ['created_at', 'updated_at', 'total_price']
    inlines = [OrderItemInline]
    date_hierarchy = 'created_at'
    list_per_page = 20

    fieldsets = (
        ('Customer Info', {
            'fields': ('user', 'first_name', 'last_name', 'email', 'phone')
        }),
        ('Shipping Address', {
            'fields': ('address', 'city', 'state', 'zip_code', 'country')
        }),
        ('Order Info', {
            'fields': ('status', 'total_price', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )