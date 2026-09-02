import pandas as pd

# Load country-level export data
input_file = "data/raw/exports_by_country_2015_2025.csv"
output_file = "data/processed/partner_hhi_2015_2025.csv"

df = pd.read_csv(input_file)

# Exclude "Other countries" because it is an aggregate,
# not a single trading partner.
partners = df[df["Country"] != "Other countries"].copy()

# Calculate HHI for each year
hhi_results = []

for year in range(2015, 2026):
    total_exports = partners[str(year)].sum()

    shares = partners[str(year)] / total_exports

    hhi = (shares ** 2).sum() * 10000

    hhi_results.append({
        "Year": year,
        "Partner_HHI": round(hhi, 2)
    })

# Create results table
hhi_df = pd.DataFrame(hhi_results)

# Save results
hhi_df.to_csv(output_file, index=False)

print("Partner HHI calculated successfully!")
print(hhi_df.to_string(index=False))