import logging
from .client import get_client

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    """
    Places a MARKET or LIMIT order on Binance Futures Testnet
    """

    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order placed successfully: {order}")
        return order

    except Exception as e:
        logging.error(f"Order placement failed: {str(e)}")
        raise
