import pandas as pd

# Load country-level export data
input_file = "data/raw/exports_by_country_2015_2025.csv"

df = pd.read_csv(input_file)

print("Country dataset loaded successfully!")
print(f"Number of countries/rows: {len(df)}")
print()

# Check the columns
print("Columns:")
print(df.columns.tolist())
print()

# Calculate total exports by country for selected years
for year in [2015, 2020, 2025]:
    total = df[str(year)].sum()

    print(
        f"{year}: {total:,.1f} thousand USD "
        f"= {total / 1000:,.1f} million USD"
    )

print()

# Show the largest export partners in 2025
top_2025 = (
    df[["Country", "2025"]]
    .sort_values("2025", ascending=False)
    .head(10)
)

print("Top 10 export destinations in 2025:")
print(top_2025.to_string(index=False))