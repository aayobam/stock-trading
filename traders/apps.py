from django.apps import AppConfig


class TradersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "traders"

    def ready(self):
        import traders.signals