from django.contrib import admin

from .models import IpItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('owner', 'type_of_item', 'number', 'title')


admin.site.register(IpItem, ItemAdmin)
