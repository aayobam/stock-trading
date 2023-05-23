from os import close
import time
import random
import json, decimal
from decimal import Decimal
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.core.management import BaseCommand, CommandError
from traders.models import Trade


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super().default(obj)


class Command(BaseCommand):
    help = 'Simulates profit and loss for traders'

    def handle(self, *args, **options):
        trades = Trade.objects.all()
        while True:
            if not trades:
                self.stdout.write(self.style.SUCCESS(f'There are no trades available to be simulated...'))

            for trade in trades:
                data_entries = []
                trade.balance = Decimal(str(trade.balance))
                profit_loss = Decimal(random.randint(-10, 10))

                if trade.balance == Decimal('0.00') or trade.balance < abs(profit_loss):
                    # Trading stops for an account with zero balanace or less then the profit_loss
                    continue

                elif trade.trader.is_superuser or trade.trader.is_staff:
                    continue
                
                trade.balance += profit_loss # adds profit or deduct loss from account balance.
                trade_data = {
                    "trader_name": str(trade.trader),
                    "balance": trade.balance,
                    "profit_loss": profit_loss,
                    "timestamp": str(datetime.now())
                }
                trade_json = json.dumps(trade_data, cls=DecimalEncoder)
                data_list = json.loads(trade_json)
                data_entries.append(data_list)
                trade.graph_data += data_entries 
                trade.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully simulated trade {trade.trader} {data_list}'))
            time.sleep(60)
