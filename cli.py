from bot.client import get_client
from bot.orders import place_market_order, place_limit_order
from bot.logger import setup_logger


def main():
    logger = setup_logger()
    client = get_client()

    print("=== Binance Spot Testnet Trading Bot ===")
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    order_type = input("Enter order type (MARKET or LIMIT): ").upper()
    quantity = input("Enter quantity: ")

    if order_type == "MARKET":
        place_market_order(client, symbol, side, quantity, logger)

    elif order_type == "LIMIT":
        price = input("Enter price: ")
        place_limit_order(client, symbol, side, quantity, price, logger)

    else:
        print("Invalid order type.")


if __name__ == "__main__":
    main()