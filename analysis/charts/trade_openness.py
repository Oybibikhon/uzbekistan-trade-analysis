import pandas as pd 
import matplotlib.pyplot as plt

# Load the processed dataset
df = pd.read_csv("data/processed/trade_indicators_2015_2025.csv")

# Create the chart
plt.figure(figsize=(10, 6))

plt.plot( 
    df["Year"], 
    df["Trade_Openness_percent"], 
    marker="o", 
    label="Trade openness" 
    )

plt.title("Uzbekistan: Trade Openness, 2015–2025") 
plt.xlabel("Year") 
plt.ylabel("Trade openness (%)") 
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the chart
plt.savefig("charts/trade_openness_2015_2025.png", dpi=300)

plt.show()