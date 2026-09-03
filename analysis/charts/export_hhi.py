import pandas as pd
import matplotlib.pyplot as plt

input_file = "data/processed/export_hhi_2015_2025.csv"
output_file = "charts/export_hhi_2015_2025.png"

print("Loading HHI data...")

df = pd.read_csv(input_file)

print(df)

plt.figure(figsize=(10, 6))

plt.plot(
    df["Year"],
    df["Export_HHI"],
    marker="o"
)

plt.title("Uzbekistan Export Concentration (HHI), 2015–2025")
plt.xlabel("Year")
plt.ylabel("Export HHI")
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(output_file, dpi=300)

print("Chart saved successfully!")
print(output_file)