from product.models import Product, Category, SubCategory, SubDescription, Color, Image, Property, Subset, IP
from django.contrib import admin


class ImageInline(admin.TabularInline):
    model = Image


class PropertyInline(admin.TabularInline):
    model = Property


class SubDescriptionInline(admin.TabularInline):
    model = SubDescription


class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline, PropertyInline, SubDescriptionInline)
    raw_id_fields = ('color',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Subset)
# admin.site.register(SubDescription)
admin.site.register(Color)
# admin.site.register(Image)
# admin.site.register(Property)
admin.site.register(IP)
