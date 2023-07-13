from django.urls import path
from api.consumers import StockPriceConsumer

ws_urlpatterns = [
    path("ws/sp/", StockPriceConsumer.as_asgi()),
]