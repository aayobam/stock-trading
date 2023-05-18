from django.contrib import admin
from .models import Trader


@admin.register(Trader)
class AdminTrader(admin.ModelAdmin):
    list_display = ('user', 'balance', 'timestamp')
    readonly_fields = ('id',)