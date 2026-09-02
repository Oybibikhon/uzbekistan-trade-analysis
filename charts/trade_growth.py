import pandas as pd 
import matplotlib.pyplot as plt

# Load the processed dataset
df = pd.read_csv("data/processed/trade_indicators_2015_2025.csv")

# Create the chart
plt.figure(figsize=(10, 6))

plt.plot( 
    df["Year"], 
    df["Export_Growth_percent"], 
    marker="o", 
    label="Export growth" 
    )

plt.plot( 
    df["Year"], 
    df["Import_Growth_percent"], 
    marker="o", 
    label="Import growth" 
    )

plt.axhline(0, linewidth=1)

plt.title("Uzbekistan: Export and Import Growth, 2015–2025") 
plt.xlabel("Year") 
plt.ylabel("Annual growth (%)") 
plt.legend() 
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the chart
plt.savefig("charts/trade_growth_2015_2025.png", dpi=300)

plt.show()