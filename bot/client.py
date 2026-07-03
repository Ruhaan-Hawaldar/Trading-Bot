from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import API_KEY, API_SECRET
from bot.logging_config import logger


class BinanceClient:
    """
    Wrapper class for Binance Futures Testnet client.
    """

    def __init__(self):
        try:
            self.client = Client(API_KEY, API_SECRET)

            # Use Binance Futures Testnet
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

            logger.info("Connected to Binance Futures Testnet.")

        except Exception as e:
            logger.error(f"Failed to initialize Binance client: {e}")
            raise

    def get_client(self):
        return self.client