from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import CustomUser
from .models import Trade


@receiver(post_save, sender=CustomUser)
def create_or_update_trade(sender, instance, created, **kwargs):
    if created:
        Trade.objects.get_or_create(trader=instance, balance=100.00)
    # else:
    #     try:
    #         trade = Trade.objects.get(trader=instance)
    #         trade.save()
    #     except Trade.DoesNotExist:
    #         pass