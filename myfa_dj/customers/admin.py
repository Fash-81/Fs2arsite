from django.contrib import admin
from .models import *




class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['case','topic','subject','content','description','created_at', 'p_image','creator']
    search_fields=['case','topic','subject','content','description','created_at','creator']

admin.site.register(Portfolio, PortfolioAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['case','topic','subject','customer','content','description','created_at', 'o_image']
    search_fields=['case','topic','subject','customer','content','description','created_at']

admin.site.register(Order, OrderAdmin)
