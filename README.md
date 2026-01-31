# Binance Futures Testnet Trading Bot (Python)

A simplified **Python CLI trading bot** that places **MARKET** and **LIMIT** orders on **Binance Futures Testnet (USDT-M)**.
Built as part of a technical assignment to demonstrate clean architecture, input validation, logging, and error handling.

---

## 🚀 Features

* Place **MARKET** and **LIMIT** orders
* Supports **BUY** and **SELL** sides
* Binance **Futures Testnet (USDT-M)** only (no real money)
* Command Line Interface (CLI)
* Structured, modular codebase
* Input validation
* Centralized logging (`logs/app.log`)

---

## 📁 Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance Futures Testnet client
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   └── cli.py             # CLI entry point
│
├── logs/
│   └── app.log            # Application logs
│
├── .env                   # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧰 Requirements

* Python **3.9+**
* Binance Futures **Testnet** account

Python packages:

* `python-binance`
* `python-dotenv`
* `click`

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-github-repo-url>
cd trading_bot
```

---

### 2️⃣ Create & activate virtual environment

**Windows (Git Bash):**

```bash
python -m venv venv
source venv/Scripts/activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\Activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure environment variables

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
```

> ⚠️ Use **Binance Futures Testnet** API keys from:
> [https://testnet.binancefuture.com](https://testnet.binancefuture.com)

---

## ▶️ How to Run

### MARKET Order Example

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

### LIMIT Order Example

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 50000
```

---

## 📤 Sample Output

```text
✅ ORDER PLACED SUCCESSFULLY
---------------------------------
Symbol        : BTCUSDT
Order ID      : 123456789
Status        : FILLED
Executed Qty  : 0.001
Avg Price     : 43210.5
```

---

## 📝 Logging

All API requests, responses, and errors are logged to:

```text
logs/app.log
```

---

## ⚠️ Error Handling

* Invalid input is rejected before API calls
* API and network errors are caught and logged
* Clear error messages are shown in CLI

---

## 📌 Assumptions

* Only **USDT-M Futures Testnet** is used
* No leverage or margin configuration included
* Bot places manual CLI-triggered orders only

---

## 🧪 Tested With

* Binance Futures Testnet
* Python 3.10 (Windows)

---

## 📄 License

MIT License

---

## 👤 Author

**Tushar Chandel**
Junior Python / Software Engineer Candidate
