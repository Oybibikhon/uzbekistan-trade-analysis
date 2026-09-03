import pandas as pd 
import matplotlib.pyplot as plt

# Load the processed dataset
df = pd.read_csv("data/processed/trade_indicators_2015_2025.csv")

# Create the chart
plt.figure(figsize=(10, 6))

plt.plot(df["Year"], df["Exports_USD_million"], marker="o", label="Exports") 
plt.plot(df["Year"], df["Imports_USD_million"], marker="o", label="Imports")

plt.title("Uzbekistan: Exports vs. Imports, 2015–2025") 
plt.xlabel("Year") 
plt.ylabel("USD million") 
plt.legend() 
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the chart
plt.savefig("charts/exports_vs_imports_2015_2025.png", dpi=300)

plt.show()