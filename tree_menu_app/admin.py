from django.contrib import admin
from .models import MenuItem
# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'menu_name')
    list_filter = ('menu_name', 'parent')
    search_fields = ('title', )

admin.site.register(MenuItem, MenuItemAdmin)
