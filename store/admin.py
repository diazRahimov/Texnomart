from django.contrib import admin
from .models import Category, Product, Image, Order, Comment, Like

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Like)
