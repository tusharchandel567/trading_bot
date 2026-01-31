import click
import logging

from .validators import validate_order
from .orders import place_order
from .logging_config import setup_logger

# Setup logging
setup_logger()

@click.command()
@click.option("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
@click.option("--side", required=True, help="BUY or SELL")
@click.option("--order_type", required=True, help="MARKET or LIMIT")
@click.option("--quantity", required=True, type=float, help="Order quantity")
@click.option("--price", required=False, type=float, help="Price (required for LIMIT orders)")
def main(symbol, side, order_type, quantity, price):
    """
    Binance Futures Testnet Trading Bot (CLI)
    """
    try:
        validate_order(symbol, side, order_type, quantity, price)

        order = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\n✅ ORDER PLACED SUCCESSFULLY")
        print("---------------------------------")
        print("Symbol        :", order.get("symbol"))
        print("Order ID      :", order.get("orderId"))
        print("Status        :", order.get("status"))
        print("Executed Qty  :", order.get("executedQty"))
        print("Avg Price     :", order.get("avgPrice"))

    except Exception as e:
        logging.error(str(e))
        print("\n❌ ERROR:", str(e))


if __name__ == "__main__":
    main()
