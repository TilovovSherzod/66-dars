from django.contrib import admin
from .models import Order, Product, Review, Category

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category)