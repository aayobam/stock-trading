from django.contrib import admin
from .models import Trade


@admin.register(Trade)
class AdminTrade(admin.ModelAdmin):
    list_display = ('trader', 'balance', 'graph_data', 'created_on', 'updated_on')
    readonly_fields = ('id', 'balance')