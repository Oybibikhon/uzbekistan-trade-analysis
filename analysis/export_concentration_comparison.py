import pandas as pd
import matplotlib.pyplot as plt

# Load product and partner HHI data
product_hhi = pd.read_csv(
    "data/processed/export_hhi_2015_2025.csv"
)

partner_hhi = pd.read_csv(
    "data/processed/partner_hhi_2015_2025.csv"
)

# Merge the two datasets by year
comparison = pd.merge(
    product_hhi,
    partner_hhi,
    on="Year"
)

print("Export concentration comparison:")
print(comparison.to_string(index=False))

# Create the comparison chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(
    comparison["Year"],
    comparison["Export_HHI"],
    marker="o",
    label="Product concentration"
)

ax.plot(
    comparison["Year"],
    comparison["Partner_HHI"],
    marker="o",
    label="Partner concentration"
)

ax.set_title(
    "Uzbekistan's Export Concentration, 2015–2025",
    fontsize=16
)

ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("HHI", fontsize=12)

ax.legend()

plt.xticks(comparison["Year"], rotation=45)

plt.tight_layout()

# Save the chart
plt.savefig(
    "charts/export_concentration_comparison_2015_2025.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Save the comparison data
comparison.to_csv(
    "data/processed/export_concentration_comparison_2015_2025.csv",
    index=False
)

print("\nExport concentration comparison saved successfully.")