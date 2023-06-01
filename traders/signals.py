from decimal import Decimal
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import CustomUser
from .models import Trade


@receiver(post_save, sender=CustomUser)
def create_or_update_trade(sender, instance, created, **kwargs):
    if created:
        balance = Decimal(str(100))
        Trade.objects.create(user=instance, balance=balance)
    else:
        trade = Trade.objects.get(user=instance)
        trade.balance = Decimal(str(100))
        trade.save()