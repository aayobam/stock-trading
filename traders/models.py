import uuid
from decimal import Decimal
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Trade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trader")
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.JSONField(default=list, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Trade"
        verbose_name_plural = "Trades"

    def __str__(self) -> str:
        return self.trader.username

    def get_absolute_url(self):
        return reverse("trade_detail", kwargs={"id": self.id})
    
    def save(self, *args, **kwargs):
        if not self.id and User.objects.count() < 10:
            self.balance = Decimal(100)
        return super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_trade(sender, instance, created, **kwargs):
    if created:
        Trade.objects.get_or_create(trader=instance)

    