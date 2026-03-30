# 📊 Capital Access & Investment Gap in Africa

> Analysing the cost of capital and investment rates across African economies to understand why private investment remains constrained — and what that means for development finance.

---

## Overview

One of the biggest barriers to growth in Africa isn't a lack of opportunity — it's the cost of accessing capital. Lending rates across much of the continent are 2–3× higher than in comparable emerging markets, making it expensive for businesses to borrow and invest.

This project uses World Bank data to visualise the investment gap across 12 African economies and compare it against global benchmarks, exploring the relationship between high borrowing costs and low investment rates.

---

## Objective

- Compare **gross capital formation (% of GDP)** across African and benchmark countries
- Visualise how **lending interest rates** relate to investment activity
- Identify which countries face the sharpest capital access constraints

---

## Tools

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| pandas | Data manipulation |
| matplotlib | Visualisation |

---

## Data Sources

**World Bank – World Development Indicators (WDI)**
- Gross capital formation (% of GDP): [`NE.GDI.TOTL.ZS`](https://data.worldbank.org/indicator/NE.GDI.TOTL.ZS)
- Lending interest rate (%): [`FR.INR.LEND`](https://data.worldbank.org/indicator/FR.INR.LEND)

Data are compiled directly in the script for reproducibility (approx. 2021–2022).

---

## How to Run

```bash
pip install pandas matplotlib
python analysis.py
```

Chart is saved to `outputs/capital_access_analysis.png`.

---

## Key Findings

- African lending rates average **~18%**, versus under 10% in benchmark economies — a structural premium that crowds out private borrowing
- **Nigeria and Ghana** face lending rates above 25%, making affordable business finance practically inaccessible for most firms
- **South Africa's investment rate (14.5% of GDP)** falls well below the ~25% threshold associated with sustained growth in emerging markets
- **Tanzania and Mozambique** show higher investment rates, but this is largely driven by public spending rather than private capital

---

## Why This Matters for Development Finance

The cost of capital is one of the first things a development finance institution (DFI) like the **AfDB** or **IFC** looks at when assessing a market. When commercial lending is too expensive, private investment dries up — which is precisely the gap that blended finance instruments (guarantees, concessional loans, first-loss facilities) are designed to fill.

---

## Output

![Capital Access Chart](outputs/capital_access_analysis.png)

---

*Part of a four-project portfolio analysing Africa's development challenges, aligned with the African Development Bank's Four Cardinal Points.*
