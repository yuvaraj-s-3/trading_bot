# Binance Spot Testnet Trading Bot  
Yuvaraj

This project is a simple command-line trading bot built using Python and the Binance Spot Testnet API.  
It demonstrates API integration, order execution, structured logging, and modular project design.

The bot allows users to place MARKET and LIMIT orders in a safe test environment (no real funds involved).

---

## What This Project Demonstrates

- Secure API authentication using environment variables
- Market order execution (BUY / SELL)
- Limit order execution (BUY / SELL)
- Exception handling for API errors
- Logging of trade activity
- Clean and modular folder structure
- Command-line interaction

This implementation focuses on clarity, correctness, and maintainability rather than trading strategy complexity.

---

## Project Structure

trading_bot/  
│  
├── bot/  
│   ├── client.py        (API connection setup)  
│   ├── orders.py        (Order execution logic)  
│   ├── logger.py        (Logging configuration)  
│  
├── logs/                (Generated trade logs)  
├── cli.py               (Application entry point)  
├── requirements.txt  
├── README.md  

---

## Setup

1. Clone the repository  
   git clone <your-repo-link>  
   cd trading_bot  

2. Create and activate virtual environment  
   python -m venv venv  
   venv\Scripts\activate  

3. Install dependencies  
   pip install -r requirements.txt  

4. Create a `.env` file in the root directory with your Binance Spot Testnet API credentials:

   BINANCE_API_KEY=your_testnet_key  
   BINANCE_API_SECRET=your_testnet_secret  

API keys can be generated from:  
https://testnet.binance.vision/

---

## Running the Bot

python cli.py

You will be prompted to enter:

- Trading pair (e.g., BTCUSDT)
- Order side (BUY or SELL)
- Order type (MARKET or LIMIT)
- Quantity
- Price (for LIMIT orders)

---

## Logging

All successful and failed trade attempts are recorded in:

logs/trades.log

This ensures traceability and basic operational monitoring.

---

## Notes

- This project is built for demonstration and assessment purposes.
- It operates only on Binance Spot Testnet.
- No real funds are used.
- No trading strategy logic is implemented — the focus is API integration and system structure.

Yuvaraj