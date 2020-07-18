from django.contrib import admin
from .models import Order


class CustPost(admin.ModelAdmin):

    list_display = ('name', 'created', 'address',)
    list_filter = ('created',)
    search_fields = ('address', 'name', 'created',)


admin.site.register(Order, CustPost)
