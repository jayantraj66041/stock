from django.urls import path
from api.consumers import StockPriceConsumer

ws_urlpatterns = [
    # API path
    path("ws/sp/", StockPriceConsumer.as_asgi()),
]