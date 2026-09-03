import pandas as pd
import matplotlib.pyplot as plt

# Load the processed trade data
df = pd.read_csv("data/processed/trade_indicators_2015_2025.csv")

# Select the relevant columns
growth = df[["Year", "Export_Growth_percent", "Import_Growth_percent"]].copy()

# Display the growth data
print(growth)

# Create the chart
plt.figure(figsize=(10, 6))

plt.plot(
    growth["Year"],
    growth["Export_Growth_percent"],
    marker="o",
    label="Export Growth"
)

plt.plot(
    growth["Year"],
    growth["Import_Growth_percent"],
    marker="o",
    label="Import Growth"
)

plt.axhline(0, linewidth=0.8)

plt.title("Uzbekistan Export and Import Growth, 2016–2025")
plt.xlabel("Year")
plt.ylabel("Growth (%)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the chart
plt.savefig("charts/trade_growth_2016_2025.png", dpi=300)

plt.show()