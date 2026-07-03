import time

from binance.exceptions import BinanceAPIException

from bot.logging_config import (
    logger,
    market_logger,
    limit_logger
)


class OrderManager:
    """
    Handles Binance Futures order placement.
    """

    def __init__(self, client):
        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None,
    ):
        """
        Place a MARKET or LIMIT order and return the latest order status.
        """

        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            logger.info(f"Order Request: {params}")

            # Place order
            response = self.client.futures_create_order(**params)

            logger.info(f"Initial Response: {response}")

            # Wait briefly so Binance updates the order status
            time.sleep(1)

            # Fetch latest order details
            order = self.client.futures_get_order(
                symbol=symbol,
                orderId=response["orderId"]
            )

            logger.info(f"Final Order Response: {order}")

            if order_type == "MARKET":
                market_logger.info(f"Order Request : {params}")
                market_logger.info(f"Order Response : {order}")

            elif order_type == "LIMIT":
                limit_logger.info(f"Order Request : {params}")
                limit_logger.info(f"Order Response : {order}")

            return {
                "orderId": order.get("orderId"),
                "status": order.get("status"),
                "executedQty": order.get("executedQty"),
                "avgPrice": order.get("avgPrice"),
            }

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            raise

        except Exception as e:
            logger.exception("Unexpected Error")
            raise