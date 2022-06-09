from django.contrib import admin
from .models import Category, Product, Subproduct, Portfolio, Call



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id_category', 'category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id_product', 'product']

@admin.register(Subproduct)
class SubproductAdmin(admin.ModelAdmin):
    list_display = [ 'subproduct', 'parent']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = [ 'picture', 'text']


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = [ 'client', 'phone', 'date']

