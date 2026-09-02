import pandas as pd

# Load product-level export data
input_file = "data/raw/exports_by_product_2015_2025.csv"
output_file = "data/processed/export_hhi_2015_2025.csv"

df = pd.read_csv(input_file)

# Exclude Services (code 99)
goods = df[df["Code"] != 99].copy()

# Calculate HHI for each year
hhi_results = []

for year in range(2015, 2026):
    total_exports = goods[str(year)].sum()
    shares = goods[str(year)] / total_exports
    hhi = (shares ** 2).sum() * 10000

    hhi_results.append({
        "Year": year,
        "Export_HHI": round(hhi, 2)
    })

# Create results table
hhi_df = pd.DataFrame(hhi_results)

# Save results
hhi_df.to_csv(output_file, index=False)

print("Export HHI calculated successfully!")
print(hhi_df.to_string(index=False))