"""
======================================
  STOCK PORTFOLIO TRACKER
  Task 2 - Python Project
======================================
  Concepts: dict, I/O, arithmetic,
            file handling
======================================
"""

import csv
import os
from datetime import datetime

# ── Hardcoded stock price dictionary ──────────────────────────────────────────
STOCK_PRICES = {
    "AAPL":  180.00,   # Apple Inc.
    "TSLA":  250.00,   # Tesla Inc.
    "GOOGL": 140.00,   # Alphabet Inc.
    "MSFT":  375.00,   # Microsoft Corp.
    "AMZN":  185.00,   # Amazon.com Inc.
    "META":  500.00,   # Meta Platforms
    "NVDA":  875.00,   # NVIDIA Corp.
    "NFLX":  625.00,   # Netflix Inc.
    "AMD":   165.00,   # Advanced Micro Devices
    "INTC":   35.00,   # Intel Corp.
}


def display_banner():
    """Print a welcome banner."""
    print("\n" + "=" * 50)
    print("       📈  STOCK PORTFOLIO TRACKER  📈")
    print("=" * 50)


def display_available_stocks():
    """Show all available stocks and their prices."""
    print("\n📋  Available Stocks:")
    print("-" * 35)
    print(f"  {'Symbol':<8} {'Company / Price':>20}")
    print("-" * 35)
    names = {
        "AAPL": "Apple Inc.",    "TSLA": "Tesla Inc.",
        "GOOGL": "Alphabet",     "MSFT": "Microsoft",
        "AMZN": "Amazon",        "META": "Meta",
        "NVDA": "NVIDIA",        "NFLX": "Netflix",
        "AMD":  "AMD",           "INTC": "Intel",
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8}  ${price:>8.2f}   {names[symbol]}")
    print("-" * 35)


def get_portfolio_from_user():
    """
    Interactively ask the user for stock symbols and quantities.
    Returns a dict { 'SYMBOL': quantity }.
    """
    portfolio = {}
    print("\n✏️   Enter your stocks (type 'done' when finished):")
    print("    Format: SYMBOL  QUANTITY  (e.g.  AAPL 10)\n")

    while True:
        raw = input("    > ").strip().upper()

        if raw in ("DONE", "D", ""):
            if not portfolio:
                print("    ⚠️  No stocks entered yet. Add at least one.")
                continue
            break

        parts = raw.split()
        if len(parts) != 2:
            print("    ❌  Please enter exactly: SYMBOL QUANTITY")
            continue

        symbol, qty_str = parts
        if symbol not in STOCK_PRICES:
            print(f"    ❌  '{symbol}' not found. Choose from the list above.")
            continue

        try:
            qty = int(qty_str)
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("    ❌  Quantity must be a positive whole number.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
            print(f"    ✅  Updated {symbol}: total = {portfolio[symbol]} shares")
        else:
            portfolio[symbol] = qty
            print(f"    ✅  Added {symbol} × {qty}")

    return portfolio


def calculate_portfolio(portfolio):
    """
    Given { symbol: qty }, return a list of row-dicts and the grand total.
    Each row: { symbol, price, quantity, value }
    """
    rows = []
    total = 0.0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        rows.append({
            "symbol":   symbol,
            "price":    price,
            "quantity": qty,
            "value":    value,
        })
    # Sort by value descending
    rows.sort(key=lambda r: r["value"], reverse=True)
    return rows, total


def display_results(rows, total):
    """Pretty-print the portfolio summary."""
    print("\n" + "=" * 55)
    print("          💼  PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"  {'Stock':<8} {'Price':>10} {'Qty':>6} {'Value':>14}")
    print("-" * 55)
    for r in rows:
        pct = (r["value"] / total) * 100
        print(f"  {r['symbol']:<8} ${r['price']:>9.2f} {r['quantity']:>6}   "
              f"${r['value']:>11,.2f}  ({pct:.1f}%)")
    print("-" * 55)
    print(f"  {'TOTAL INVESTMENT':<30}  ${total:>12,.2f}")
    print("=" * 55)


def save_to_txt(rows, total, filename="portfolio_result.txt"):
    """Save the portfolio summary as a .txt file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO TRACKER - RESULT\n")
        f.write(f"Generated: {timestamp}\n")
        f.write("=" * 55 + "\n")
        f.write(f"{'Stock':<8} {'Price':>10} {'Qty':>6} {'Value':>14}\n")
        f.write("-" * 55 + "\n")
        for r in rows:
            pct = (r["value"] / total) * 100
            f.write(f"{r['symbol']:<8} ${r['price']:>9.2f} {r['quantity']:>6}   "
                    f"${r['value']:>11,.2f}  ({pct:.1f}%)\n")
        f.write("-" * 55 + "\n")
        f.write(f"{'TOTAL INVESTMENT':<30}  ${total:>12,.2f}\n")
        f.write("=" * 55 + "\n")
    print(f"\n  💾  Saved to '{filename}'")


def save_to_csv(rows, total, filename="portfolio_result.csv"):
    """Save the portfolio data as a .csv file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock Portfolio Tracker"])
        writer.writerow(["Generated:", timestamp])
        writer.writerow([])
        writer.writerow(["Symbol", "Price (USD)", "Quantity", "Total Value (USD)", "% of Portfolio"])
        for r in rows:
            pct = round((r["value"] / total) * 100, 2)
            writer.writerow([r["symbol"], r["price"], r["quantity"],
                             round(r["value"], 2), pct])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", round(total, 2), "100.00"])
    print(f"  💾  Saved to '{filename}'")


def ask_save_option(rows, total):
    """Ask the user if they want to save results and in which format."""
    print("\n  💾  Save results?")
    print("     [1] Save as .txt")
    print("     [2] Save as .csv")
    print("     [3] Save both")
    print("     [4] Don't save")

    choice = input("\n  Your choice (1-4): ").strip()
    if choice == "1":
        save_to_txt(rows, total)
    elif choice == "2":
        save_to_csv(rows, total)
    elif choice == "3":
        save_to_txt(rows, total)
        save_to_csv(rows, total)
    else:
        print("  ℹ️   Results not saved.")


def main():
    display_banner()
    display_available_stocks()

    portfolio = get_portfolio_from_user()
    rows, total = calculate_portfolio(portfolio)
    display_results(rows, total)
    ask_save_option(rows, total)

    print("\n  👋  Thanks for using Stock Portfolio Tracker!\n")


if __name__ == "__main__":
    main()