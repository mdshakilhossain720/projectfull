from django.contrib import admin
from.models import Product,Customer

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model=Product
        fields="__all__"

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    class Meta:
        model=Customer
        fields="__all__"

