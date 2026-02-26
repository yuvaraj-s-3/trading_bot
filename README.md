\# Trading Bot Assignment



\## Description

This project is a simple Python-based trading bot using the Binance API.

It demonstrates local development using Python, virtual environments,

modular code structure, and GitHub version control.



\## Features

\- Binance API client initialization

\- Environment variable based API key loading

\- CLI-based execution

\- Modular bot architecture



\## Project Structure

trading\_bot/

├── bot/

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   ├── logging\_config.py

├── cli.py

├── requirements.txt

├── README.md



\## Setup Instructions

1\. Install Python 3.11+

2\. Create virtual environment:

&nbsp;  python -m venv venv

3\. Activate venv

4\. Install dependencies:

&nbsp;  pip install -r requirements.txt

5\. Add API keys in `.env`

6\. Run the bot:

&nbsp;  python cli.py

