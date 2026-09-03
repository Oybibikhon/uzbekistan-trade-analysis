import pandas as pd
import matplotlib.pyplot as plt

# Load partner HHI results
input_file = "data/processed/partner_hhi_2015_2025.csv"

df = pd.read_csv(input_file)

# Create the chart
plt.figure(figsize=(10, 6))

plt.plot(
    df["Year"],
    df["Partner_HHI"],
    marker="o"
)

plt.title("Uzbekistan Export Partner Concentration, 2015–2025")
plt.xlabel("Year")
plt.ylabel("Partner HHI")
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the chart
plt.savefig(
    "charts/partner_hhi_2015_2025.png",
    dpi=300
)

plt.show()