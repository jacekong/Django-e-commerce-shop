from django.contrib import admin
from .models import Product, Category, ProductImage
from .models import Comment, ClientViews

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display        = ('product_name', 'product_code', 'factory_price', 'selling_price', 'stock_status', 'category', )
    search_fields       = ('product_name', 'product_code',)
    list_filter         = ('category',)
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat_title',)}
    list_filter         = ('cat_title',)

class ImageAdmin(admin.ModelAdmin):
    list_display        = ('products',)

class CommentAdmin(admin.ModelAdmin):
    list_display        = ('product', 'comment', 'date_created')

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('ip_addr', 'device_type', 'views_time', 'view_date',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ClientViews, ClientsAdmin)
