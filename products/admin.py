from django.contrib import admin
from .models import homeutilities,Fooditems,beverages,grocery

# Register your models here.
admin.site.register(beverages)
admin.site.register(Fooditems)
admin.site.register(homeutilities)
admin.site.register(grocery)