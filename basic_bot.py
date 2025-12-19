import logging
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logging.info("Connected to Binance Futures Testnet")

    def set_leverage(self, symbol, leverage=1):
        self.client.futures_change_leverage(
            symbol=symbol,
            leverage=leverage
        )

    def place_market_order(self, symbol, side, quantity):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    def place_limit_order(self, symbol, side, quantity, price):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
