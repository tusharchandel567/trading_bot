import os
from binance.client import Client
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def get_client():
    """
    Returns a Binance Futures Testnet client
    """
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise RuntimeError("API keys not found. Check your .env file.")

    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True
    )

    # Futures testnet base URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
