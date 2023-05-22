from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)

@shared_task
def simulate_trade_task():
    call_command("simulate_trade")
    logger.info("Added task to queue and simulating task...")
    return "Done"

