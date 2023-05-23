import uuid
from django.db import models
from django.urls import reverse
from users.models import CustomUser
from common.models import TimeStampedModel


class Trade(TimeStampedModel):
    trader = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="trader")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    graph_data = models.JSONField(default=list, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Trade"
        verbose_name_plural = "Trades"
        ordering = ['trader__email']

    def __str__(self) -> str:
        return self.trader.email
    
    def get_absolute_url(self):
        return reverse("trade_detail", kwargs={"id": self.id})
