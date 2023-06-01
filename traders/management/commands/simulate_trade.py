import time
import random
import json, decimal
from decimal import Decimal
from datetime import datetime
from django.core.management import BaseCommand
from traders.models import Trade


# Converts instance of decimal to string
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super().default(obj)


# This automates the trading once the commabd is ran on thr command line
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
                
                # Excludes profile with 0 balance or balance less than thr loss from being simulated for trading
                if trade.balance == Decimal('0.00') or trade.balance < abs(profit_loss):
                    # Trading stops for an account with zero balanace or less then the profit_loss
                    continue
                
                # excludes staff or admin profiles from trading
                elif trade.user.is_superuser or trade.user.is_staff:
                    continue
                
                trade.balance += profit_loss # Adds profit or deduct loss from account balance.
                trade_data = {
                    "trader_name": str(trade.user),
                    "balance": trade.balance,
                    "profit_loss": profit_loss,
                    "timestamp": str(datetime.now())
                }
                # Converts to json data
                trade_json = json.dumps(trade_data, cls=DecimalEncoder)
                
                # converts to python dictionary
                data_list = json.loads(trade_json)
                
                data_entries.append(data_list)
                trade.graph_data += data_entries 
                trade.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully simulated trade {trade.user} {data_list}'))
            time.sleep(60)
