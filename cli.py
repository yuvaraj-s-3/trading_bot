from bot.client import get_client

def main():
    print("Trading bot starting...")

    client = get_client()

    symbol = "BTCUSDT"
    quantity = 0.001  # tiny test amount

    order = client.create_order(
        symbol=symbol,
        side="BUY",
        type="MARKET",
        quantity=quantity
    )

    print("ORDER PLACED SUCCESSFULLY")
    print(order)

if __name__ == "__main__":
    main()