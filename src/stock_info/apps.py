from django.apps import AppConfig


class StockInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock_info'

    # def ready(self):
    #     from .tasks import get_stock_price
    #     get_stock_price.delay()
