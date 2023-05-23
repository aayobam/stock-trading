from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import CustomUser
from .models import Trade


@receiver(post_save, sender=CustomUser)
def create_or_update_trade(sender, instance, created, **kwargs):
    if created:
        Trade.objects.create(trader=instance, balance=100.00)
    else:
        trade = Trade.objects.get(trader=instance)
        trade.balance = 100.00
        trade.save()