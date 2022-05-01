from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product']


admin.site.register(Products, AdminProduct)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
