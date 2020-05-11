from django.contrib import admin
from .models import ShopType, Shop

# Register your models here.

@admin.register(ShopType)
class ShopTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shop_type', 'get_read_num', 'content')

#@admin.register(ReadNum)
#class ReadNumAdmin(admin.ModelAdmin):
 #   list_display = ('read_num', 'shop')