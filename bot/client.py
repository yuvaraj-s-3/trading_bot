import os
from dotenv import load_dotenv
from binance.client import Client

def get_client():
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise RuntimeError("API keys not loaded")

    client = Client(
        api_key,
        api_secret,
        testnet=True
    )

    return client