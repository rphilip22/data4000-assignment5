# DATA4000 Assignment 5

This repository contains two Python programs that integrate:

- Conditionals (`if / elif / else`)
- Loops (`while`)
- Exception handling (`try / except`)
- Functions
- Python libraries (`requests`)
- Command-line interaction
- Basic API usage

---

## Installation Requirement

This project requires Python 3.x.

For Exercise 2, you must install the `requests` library:

```bash
pip install requests
```

---

# Exercise 1 — Point-of-Sale Checkout System  
**File:** `pos_checkout.py`

## Description

This program simulates a campus retail store checkout system.  
Cashiers enter purchased items, and the system calculates:

- Subtotal
- Total units
- Discount eligibility
- Seed-based member perk
- Final total

The program safely handles invalid input and never crashes.

---

## How to Run

From the terminal inside your project folder:

```bash
python pos_checkout.py
```

---

## Example Run

```
Student key: 515
Item name (or DONE): Rice
Unit price: 4
Quantity: 40
Item name (or DONE): Wheat
Unit price: 9
Quantity: 10
Item name (or DONE): Cookies
Unit price: 12
Quantity: 33
Item name (or DONE): DONE

Seed: 155
Units: 83
Subtotal: $646.00
Discount: 10%
Perk applied: YES
Total: $578.40
```

---

# Exercise 2 — Inventory Reorder Analyzer with API Spot Check  
**File:** `inventory_spotcheck.py`

## Description

This program simulates an operations inventory tool.

It:

- Accepts SKU entries
- Validates inventory levels
- Determines reorder status using seed-based threshold logic
- Performs an external API spot check using the iTunes Search API
- Counts returned songs
- Handles network and JSON errors safely

---

## How to Run

First ensure `requests` is installed:

```bash
pip install requests
```

Then run:

```bash
python inventory_spotcheck.py
```

---

## Example Run

```
Student key: 515
SKU: ABC123
On hand: 5
SKU: XYZ789
On hand: 20
SKU: DONE

Seed: 155
Threshold: 12
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: drake
Songs returned: 5
API status: OK
```

If the API fails (network issue), the output will show:

```
Songs returned: N/A
API status: FAILED
```
---