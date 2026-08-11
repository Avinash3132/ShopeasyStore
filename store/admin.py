from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ['image', 'alt_text', 'order', 'preview']
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="80" '
                'style="object-fit:cover; border-radius:6px;" />',
                obj.image.url
            )
        return mark_safe('<span style="color:#94a3b8;">No image</span>')
    preview.short_description = 'Preview'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_count']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

    def product_count(self, obj):
        count = obj.products.count()
        return format_html(
            '<span style="background:#dbeafe; color:#1e40af; '
            'padding:2px 8px; border-radius:50px; font-weight:600;">'
            '{}</span>',
            count
        )
    product_count.short_description = 'Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'thumbnail', 'name', 'category', 'price',
        'stock', 'available', 'featured', 'gallery_count'
    ]
    list_filter = ['available', 'featured', 'category', 'created_at']
    list_editable = ['price', 'stock', 'available', 'featured']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_per_page = 20
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at', 'thumbnail_preview']
    inlines = [ProductImageInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'slug', 'description')
        }),
        ('Pricing', {
            'fields': ('price', 'old_price')
        }),
        ('Inventory', {
            'fields': ('stock', 'available', 'featured')
        }),
        ('Main Image', {
            'fields': ('image', 'thumbnail_preview'),
            'description': 'Primary product image shown in listings.'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="45" height="45" '
                'style="object-fit:cover; border-radius:8px; '
                'border:2px solid #e2e8f0;" />',
                obj.image.url
            )
        return mark_safe(
            '<div style="width:45px; height:45px; background:#f1f5f9; '
            'border-radius:8px; display:flex; align-items:center; '
            'justify-content:center; color:#94a3b8; font-size:0.75rem;">'
            'No img</div>'
        )
    thumbnail.short_description = 'Image'

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="200" '
                'style="object-fit:cover; border-radius:8px;" />',
                obj.image.url
            )
        return 'No image uploaded'
    thumbnail_preview.short_description = 'Preview'

    def gallery_count(self, obj):
        count = obj.gallery_images.count()
        if count > 0:
            return format_html(
                '<span style="background:#d1fae5; color:#065f46; '
                'padding:2px 8px; border-radius:50px; font-weight:600;">'
                '{} images</span>',
                count
            )
        return mark_safe(
            '<span style="background:#f1f5f9; color:#94a3b8; '
            'padding:2px 8px; border-radius:50px; font-weight:600;">'
            'No images</span>'
        )
    gallery_count.short_description = 'Gallery'