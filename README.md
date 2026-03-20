# Stock Portfolio Tracker 📈


A beginner-friendly Python project that lets users build a stock portfolio, calculate total investment value, and optionally export results to .txt or .csv.


# File Tree: CodeAlpha_Stock_Portfolio_Tracker

```
🗂️ Stock_Portfolio_Tracker
|
├── 🐍 stock_tracker.py          # Main program
├── 📄 portfolio_result.csv      # (generated on save)
├── 📄 portfolio_result.txt      # (generated on save)
└── 📝 README.md
```


##  Concepts Used 📊

| Concept                | How it's Used                                            |
|------------------------|-----------------------------------------------------------|
| Dictionary             | Hardcoded `STOCK_PRICES` dict maps symbols → prices       |
| User Input / Output    | `input()` collects stock symbols & quantities             |
| Basic Arithmetic       | price × quantity per stock, summed to total               |
| File Handling          | Optional save to `.txt` and/or `.csv`                     |



## How to Run  🚀
  
bashpython stock_tracker.py

## 📋 Available Stocks

| Symbol | Company                     | Price (USD) |
|--------|-----------------------------|-------------|
| AAPL   | Apple Inc.                  | $180.00     |
| TSLA   | Tesla Inc.                  | $250.00     |
| GOOGL  | Alphabet Inc.               | $140.00     |
| MSFT   | Microsoft Corp.             | $375.00     |
| AMZN   | Amazon.com                  | $185.00     |
| META   | Meta Platforms              | $500.00     |
| NVDA   | NVIDIA Corp.                | $875.00     |
| NFLX   | Netflix Inc.                | $625.00     |
| AMD    | Advanced Micro Devices      | $165.00     |
| INTC   | Intel Corp.                 | $35.00      |

## 💻 Sample Session

<p align="center">
  <b>📈 STOCK PORTFOLIO TRACKER 📈</b><br>
  <sub>Simulated CLI Output</sub>
</p>

```bash
==================================================
       📈  STOCK PORTFOLIO TRACKER  📈
==================================================

📋  Available Stocks:
-----------------------------------
  Symbol            Company / Price
-----------------------------------
  AAPL          $180.00   Apple Inc.
  TSLA          $250.00   Tesla Inc.
  ...

✏️   Enter your stocks (type 'done' when finished):
    Format: SYMBOL  QUANTITY  (e.g.  AAPL 10)

    > AAPL 10
    ✅  Added AAPL × 10
    > TSLA 5
    ✅  Added TSLA × 5
    > NVDA 2
    ✅  Added NVDA × 2
    > done



| 📊 Stock | 💲 Price | 📦 Qty | 💰 Value     | 📈 Allocation |
|----------|---------|--------|--------------|--------------|
| NVDA     | $875.00 | 2      | $1,750.00    | 🟢 36.1%     |
| TSLA     | $250.00 | 5      | $1,250.00    | 🟡 25.8%     |
| AAPL     | $180.00 | 10     | $1,800.00    | 🔵 37.1%     |
|----------|---------|--------|--------------|--------------|
| **TOTAL**|         |        | **$4,840.00**|              |