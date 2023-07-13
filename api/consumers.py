from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from random import randint
from time import sleep
import json
from api.models import TradeHistory


class StockPriceConsumer(SyncConsumer):
    def websocket_connect(self, event):
        # Connection stablished
        print("Websocket Connected...", event)
        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print("Websocket Receive...", event)
        print(event['text'])
        while True:
            actual_price = 10000        # base price of a stock
            stock_price = randint(9000, 11000)      # random price generated between 9000 and 11000

            # save the stock price in every updation
            th = TradeHistory()
            th.bank_name = "ABC Bank"
            th.trade_value = stock_price
            th.save()

            # call all 100 latest tradehistory and find the average price
            all_th = TradeHistory.objects.all().order_by("-id")[:100]
            avg = 0
            for th in all_th:
                avg += th.trade_value
            avg = avg/100

            # Send the response to the client
            self.send({
                "type": "websocket.send", 
                'text': json.dumps({
                    "Stock Price": stock_price,
                    "Average Price": avg,
                    "Suggestion": "Sale" if avg>actual_price else "Buy"
                })
            })

            sleep(2)

    def websocket_disconnect(self, event):
        # connection disconnected.
        print("Websocket Disconnect...", event)
        raise StopConsumer()