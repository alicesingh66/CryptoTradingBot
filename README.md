# Binance Futures Testnet Trading Bot

## Overview

This project is a **simplified trading bot** built as part of a hiring assignment. It interacts with the **Binance Futures Testnet (USDT-M)** using the official Binance API and demonstrates order placement, error handling, logging, and user interaction through both backend logic and a lightweight UI.

The bot is designed with **clean structure, reusability, and clarity**, focusing on correctness rather than overengineering.

---

## Features

* Uses **Binance Futures Testnet** (`https://testnet.binancefuture.com`)
* Supports **Market** and **Limit** orders
* Supports both **BUY** and **SELL** sides
* Interactive **Tkinter-based GUI** for user input
* Handles Futures-specific requirements (leverage initialization)
* Graceful error handling and defensive API response parsing
* Logging-ready architecture for API requests and errors

---

## Project Structure

```
BINOMO/
│── basic_bot.py     # Core trading logic (Binance Futures API)
│── gui_bot.py       # Tkinter-based UI
│── trading_bot.log  # Log file (auto-generated)
│── README.md
```

---

## Requirements

* Python 3.9+
* `python-binance` library

Install dependencies:

```bash
pip install python-binance
```

---

## Binance Testnet Setup (Important)

1. Register and activate a **Binance Futures Testnet** account
2. Generate **API Key** and **API Secret**
3. Enable **Futures permission** for the API key
4. Fund the **Futures Testnet Wallet (USDT)** using the faucet

> Note: Spot Testnet balance is different from Futures Testnet balance.

---

## How to Run the Bot

From the project directory:

```bash
python gui_bot.py
```

A Tkinter window will open where you can:

1. Enter API Key and API Secret
2. Enter trading symbol (e.g. `ETHUSDT`)
3. Select order side (BUY / SELL)
4. Select order type (MARKET / LIMIT)
5. Enter quantity (and price for LIMIT orders)
6. Place the order and view the execution response

---

## Order Types

### Market Order

* Executes immediately at market price
* No price input required

### Limit Order

* Executes at a specified price
* Requires price input

---

## Known Testnet Behavior

On **new Binance Futures Testnet accounts**, order placement APIs may return an **empty response (`{}`)** until:

* The Futures wallet is funded
* Leverage is initialized at least once

This behavior is handled defensively in the code to avoid runtime crashes.

---

## Logging

The bot is structured to support logging of:

* API calls
* Responses
* Errors

Logs are written to:

```
trading_bot.log
```

---

## Notes

* This project is intended for **educational and evaluation purposes only**
* All trades occur on **Binance Futures Testnet**, not real markets

---

## Summary

This assignment demonstrates:

* Correct use of Binance Futures API
* Clean Python code structure
* User input handling via GUI
* Awareness of real-world API edge cases

The focus is on **robustness, clarity, and correctness**, aligned with real-world development practices.
