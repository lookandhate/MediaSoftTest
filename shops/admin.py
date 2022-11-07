from django.contrib import admin
from shops.models import *


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass
