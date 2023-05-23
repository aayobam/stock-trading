from django.contrib import admin
from .models import Trade


@admin.register(Trade)
class AdminTrade(admin.ModelAdmin):
    list_display = ('id', 'trader', 'balance', 'created_on', 'updated_on')
    readonly_fields = ('id', 'balance', 'graph_data')