import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Trade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trader")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    graph_data = models.JSONField(default=list, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Trade"
        verbose_name_plural = "Trades"

    def __str__(self) -> str:
        return self.trader.username
    
    def get_absolute_url(self):
        return reverse("trade_detail", kwargs={"id": self.id})
