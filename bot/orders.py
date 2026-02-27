from binance.exceptions import BinanceAPIException

def place_market_order(client, symbol, side, quantity, logger):
    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET ORDER SUCCESS: {order}")
        print("Market order executed successfully.")
        print(order)
        return order

    except BinanceAPIException as e:
        logger.error(f"MARKET ORDER FAILED: {e}")
        print("Market order failed:", e)


def place_limit_order(client, symbol, side, quantity, price, logger):
    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )

        logger.info(f"LIMIT ORDER SUCCESS: {order}")
        print("Limit order placed successfully.")
        print(order)
        return order

    except BinanceAPIException as e:
        logger.error(f"LIMIT ORDER FAILED: {e}")
        print("Limit order failed:", e)