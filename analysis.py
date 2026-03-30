# ============================================================
# Project: Capital Access & Investment Gap in Africa
# Data:    World Bank World Development Indicators (WDI)
# Charts:  1. Investment rate (% GDP) by country
#          2. Lending rate vs investment rate scatter
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ── DATA ────────────────────────────────────────────────────
# Gross capital formation (% of GDP) — World Bank: NE.GDI.TOTL.ZS
# Lending interest rate (%)          — World Bank: FR.INR.LEND
# Reference year: approx. 2021–2022

data = {
    "Country": [
        "Nigeria", "Ethiopia", "Kenya", "Ghana", "Côte d'Ivoire",
        "Tanzania", "Mozambique", "Zambia", "Senegal", "Rwanda",
        "South Africa", "Egypt",
        "China", "India", "Brazil", "Germany"          # benchmarks
    ],
    "Region": [
        "Africa", "Africa", "Africa", "Africa", "Africa",
        "Africa", "Africa", "Africa", "Africa", "Africa",
        "Africa", "Africa",
        "Benchmark", "Benchmark", "Benchmark", "Benchmark"
    ],
    "Investment_pct_GDP": [
        26.4, 32.1, 18.2, 13.7, 22.5,
        33.4, 41.2, 28.6, 25.3, 26.0,
        14.5, 15.0,
        43.5, 31.0, 18.5, 22.8
    ],
    "Lending_Rate_pct": [
        28.4, 14.5, 12.5, 28.5, 6.5,
        16.5, 20.0, 25.7, 7.5, 16.0,
        9.75, 19.5,
        4.35, 9.2, 12.4, 1.8
    ]
}

df = pd.DataFrame(data)
africa     = df[df["Region"] == "Africa"].copy()
benchmarks = df[df["Region"] == "Benchmark"].copy()

# ── CHART 1: Investment rate bar chart ──────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Capital Access & Investment Gap in Africa", fontsize=14, fontweight="bold")

# Sort by investment rate for cleaner display
africa_sorted = africa.sort_values("Investment_pct_GDP")

ax1 = axes[0]
colors = ["#1a6e5c" if v >= 25 else "#e05c2a" for v in africa_sorted["Investment_pct_GDP"]]
ax1.barh(africa_sorted["Country"], africa_sorted["Investment_pct_GDP"],
         color=colors, edgecolor="white")

# Reference line at 25% — commonly cited minimum for sustained growth
ax1.axvline(25, color="#333333", linestyle="--", linewidth=1.2, label="25% growth benchmark")
ax1.set_xlabel("Gross Capital Formation (% of GDP)")
ax1.set_title("Investment Rate by Country", fontweight="bold")
ax1.legend(fontsize=8)
ax1.spines[["top", "right"]].set_visible(False)
ax1.xaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))

# ── CHART 2: Lending rate vs investment rate scatter ─────────
ax2 = axes[1]

# Plot African countries
for _, row in africa.iterrows():
    ax2.scatter(row["Lending_Rate_pct"], row["Investment_pct_GDP"],
                color="#1a6e5c", s=80, zorder=3)
    ax2.annotate(row["Country"], (row["Lending_Rate_pct"], row["Investment_pct_GDP"]),
                 textcoords="offset points", xytext=(5, 3), fontsize=7, color="#1a6e5c")

# Plot benchmarks in grey
for _, row in benchmarks.iterrows():
    ax2.scatter(row["Lending_Rate_pct"], row["Investment_pct_GDP"],
                color="#aaaaaa", s=80, marker="D", zorder=3)
    ax2.annotate(row["Country"], (row["Lending_Rate_pct"], row["Investment_pct_GDP"]),
                 textcoords="offset points", xytext=(5, 3), fontsize=7, color="#888888")

ax2.set_xlabel("Lending Interest Rate (%)")
ax2.set_ylabel("Investment Rate (% GDP)")
ax2.set_title("Cost of Capital vs. Investment Rate", fontweight="bold")
ax2.spines[["top", "right"]].set_visible(False)

# Shade the "high cost, low investment" problem quadrant
ax2.axhspan(0, 20, xmin=0.45, alpha=0.06, color="#e05c2a")
ax2.text(18, 5, "High cost /\nLow investment", fontsize=7.5,
         color="#e05c2a", style="italic")

plt.tight_layout()

# ── SAVE ────────────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/capital_access_analysis.png", dpi=150, bbox_inches="tight")
print("Saved: outputs/capital_access_analysis.png")
plt.show()

# ── SUMMARY ─────────────────────────────────────────────────
print("\n── Key Numbers ─────────────────────────────────────")
print(f"Avg lending rate   — Africa:     {africa['Lending_Rate_pct'].mean():.1f}%")
print(f"Avg lending rate   — Benchmarks: {benchmarks['Lending_Rate_pct'].mean():.1f}%")
print(f"Avg investment rate — Africa:     {africa['Investment_pct_GDP'].mean():.1f}% of GDP")
print(f"Avg investment rate — Benchmarks: {benchmarks['Investment_pct_GDP'].mean():.1f}% of GDP")
below_25 = africa[africa["Investment_pct_GDP"] < 25]["Country"].tolist()
print(f"\nCountries below 25% investment threshold: {', '.join(below_25)}")
