import argparse
from binance.exceptions import BinanceAPIException

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g., BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (required for LIMIT orders)"
    )

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if order_type == "LIMIT":
            print(f"Price      : {price}")

        print("===================================")

        client = BinanceClient().get_client()
        order_manager = OrderManager(client)

        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        print("\n✅ ORDER PLACED SUCCESSFULLY")
        print("----------------------------")
        print(f"Order ID      : {response['orderId']}")
        print(f"Status        : {response['status']}")
        print(f"Executed Qty  : {response['executedQty']}")
        print(f"Average Price : {response['avgPrice']}")

    except BinanceAPIException as e:
        print(f"\n❌ Binance API Error: {e.message}")

    except ValueError as e:
        print(f"\n❌ Validation Error: {e}")

    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()