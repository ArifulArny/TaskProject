from django.contrib import admin

from .models import User, Shop, ProductCategory, ProductColor, Product, CartItem, Order

admin.site.register(User)
admin.site.register(Shop)
admin.site.register(ProductCategory)
admin.site.register(ProductColor)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)

