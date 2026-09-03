import pandas as pd

# Load the product-level export data
df = pd.read_csv("data/raw/exports_by_product_2015_2025.csv")

print(df.head())

# Calculate each product category's share of total exports
years = [str(year) for year in range(2015, 2026)]

shares = df.copy()

for year in years:
    shares[year] = shares[year] / df[year].sum() * 100

print(shares[["Product_Category"] + years])

# Check that shares for each year add up to 100%
print("\nShare totals by year:")
print(shares[years].sum())

import matplotlib.pyplot as plt

# Prepare the data
chart_data = shares.set_index("Product_Category")[years].T

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))

# Positions of the years
x = range(len(years))

# Start of each stacked section
bottom = [0] * len(years)

# Create stacked bars
for category in chart_data.columns:
    values = chart_data[category].values

    ax.bar(
        x,
        values,
        bottom=bottom,
        label=category,
        width=0.75
    )

    bottom = [b + v for b, v in zip(bottom, values)]

# Formatting
ax.set_title(
    "Uzbekistan's Export Structure by Product Category, 2015–2025",
    fontsize=16
)

ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Share of Total Exports (%)", fontsize=12)

# EXACTLY 0–100%
ax.set_ylim(0, 100)
ax.set_yticks([0, 20, 40, 60, 80, 100])

# Years on x-axis
ax.set_xticks(list(x))
ax.set_xticklabels(years)

# Legend
ax.legend(
    title="Product Category",
    bbox_to_anchor=(0.5, -0.15),
    loc="upper center",
    ncol=2,
    fontsize=9
)

plt.tight_layout()

# Save
plt.savefig(
    "charts/export_structure_2015_2025.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Calculate absolute and percentage changes between 2015 and 2025

comparison = pd.DataFrame({
    "Product_Category": df["Product_Category"],
    "Export_2015": df["2015"],
    "Export_2025": df["2025"]
})

comparison["Change_USD_million"] = (
    comparison["Export_2025"] - comparison["Export_2015"]
)

comparison["Change_percent"] = (
    comparison["Change_USD_million"] /
    comparison["Export_2015"] * 100
)

# Sort by absolute change
comparison = comparison.sort_values(
    "Change_USD_million",
    ascending=False
)

print("\nExport value changes, 2015–2025:")
print(comparison.to_string(index=False))

# Save the 2015-2025 export comparison
comparison.to_csv(
    "data/processed/export_product_changes_2015_2025.csv",
    index=False
)

print("\nExport product changes saved successfully.")
