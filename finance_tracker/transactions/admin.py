from django.contrib import admin
from .models import Transaction, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  

admin.site.register(Transaction)
admin.site.register(Category, CategoryAdmin)
