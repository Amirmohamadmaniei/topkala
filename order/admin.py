from django.contrib import admin

from order.models import Order, OrderItem, Coupon


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    list_filter = ('is_paid',)


admin.site.register(Coupon)
