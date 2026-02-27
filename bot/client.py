import os
import time
from dotenv import load_dotenv
from binance.client import Client

def get_client():
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise Exception("API keys not found")

    client = Client(api_key, api_secret)
    client.API_URL = "https://testnet.binance.vision/api"

    # Fix timestamp drift
    server_time = client.get_server_time()
    system_time = int(time.time() * 1000)
    client.timestamp_offset = server_time['serverTime'] - system_time

    return client