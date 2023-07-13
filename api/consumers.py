from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from random import randint
from time import sleep


class StockPriceConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected...", event)
        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print("Websocket Receive...", event)
        print(event['text'])
        while True:
            stock_price = randint(9000, 11000)
            self.send({
                "type": "websocket.send", 
                'text': "Stock Price: " + str(stock_price)
            })
            sleep(1)

    def websocket_disconnect(self, event):
        print("Websocket Disconnect...", event)
        raise StopConsumer()