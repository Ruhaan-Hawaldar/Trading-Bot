# Binance Futures Testnet Trading Bot

A Python-based command-line trading bot that places **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**. The application follows a modular architecture with input validation, logging, and exception handling.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports **BUY** and **SELL** orders
- Command Line Interface (CLI) using `argparse`
- Input validation
- Structured project architecture
- Logging to files
- Exception handling for API and validation errors
- Binance Futures Testnet integration

---

## Project Structure

```
Trading Bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py              # Binance client wrapper
│   ├── orders.py              # Order placement logic
│   ├── validators.py          # Input validation
│   └── logging_config.py      # Logging configuration
│
├── logs/
│   ├── trading.log
│   ├── market_order.log
│   └── limit_order.log
│
├── cli.py                     # CLI entry point
├── config.py                  # Environment configuration
├── requirements.txt
├── README.md
├── .env                       # API credentials (Not committed)
└── .gitignore
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- Testnet API Key & Secret

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/trading-bot.git
cd trading-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_TESTNET_API_KEY
API_SECRET=YOUR_TESTNET_API_SECRET
```

---

## Running the Application

### MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### MARKET SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

### LIMIT BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

---

### LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## Example Output

```
========== ORDER REQUEST ==========
Symbol     : BTCUSDT
Side       : BUY
Type       : MARKET
Quantity   : 0.001
===================================

✅ ORDER PLACED SUCCESSFULLY

Order ID      : 18708222464
Status        : FILLED
Executed Qty  : 0.0010
Average Price : 61861.000000
```

---

## Logging

Logs are automatically generated inside the `logs/` directory.

- `trading.log` → Complete application logs
- `market_order.log` → MARKET order logs
- `limit_order.log` → LIMIT order logs

Example log entry:

```
2026-07-03 17:13:20 | INFO | Order Request : {'symbol': 'BTCUSDT', 'side': 'BUY'}
2026-07-03 17:13:23 | INFO | Order Response : {'status': 'FILLED'}
```

---

## Error Handling

The application handles:

- Invalid symbol
- Invalid order type
- Invalid order side
- Invalid quantity
- Missing LIMIT price
- Binance API exceptions
- Network failures
- Unexpected runtime exceptions

---

## Assumptions

- Only **USDT-M Futures** are supported.
- LIMIT orders require a price.
- User has sufficient Testnet balance.
- API credentials are stored securely in the `.env` file.

---

## Technologies Used

- Python 3
- python-binance
- argparse
- logging
- python-dotenv

---

## Future Improvements

- Stop-Limit Orders
- OCO Orders
- Interactive CLI using Typer
- Web Dashboard (Streamlit/Flask)
- Order History
- Position Monitoring

---

## Author

Ruhaan Hawaldar
