from django.core.management.base import BaseCommand
from traders.models import Trade
import random
from datetime import datetime
from time import sleep


class Command(BaseCommand):
    help = 'Simulates profit and loss for traders'

    def handle(self, *args, **options):
        trades = Trade.objects.all()
        while True:
            for trade in trades:
                profit_loss = random.randint(-100, 100)
                trade.balance += profit_loss
                trade.timestamp.append(datetime.now())
                trade.save()
            sleep(60)  # Wait for 1 minute
