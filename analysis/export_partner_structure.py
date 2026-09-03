import pandas as pd

# Load the country-level export data
df = pd.read_csv("data/raw/exports_by_country_2015_2025.csv")

print(df.head())

# Years included in the analysis
years = [str(year) for year in range(2015, 2026)]

# Calculate each country's share of total exports
shares = df.copy()

for year in years:
    shares[year] = shares[year] / df[year].sum() * 100

# Check that country shares add up to 100% each year
print("\nShare totals by year:")
print(shares[years].sum())

# Show the largest export partners in 2025
top_2025 = shares[["Country", "2025"]].sort_values(
    "2025",
    ascending=False
)

print("\nTop export partners in 2025:")
print(top_2025.head(10).to_string(index=False))

import matplotlib.pyplot as plt

# Select the top 10 individual export partners in 2025
top_countries = top_2025[
    top_2025["Country"] != "Other countries"
].head(10)["Country"]

# Prepare data for the chart
chart_data = shares[
    shares["Country"].isin(top_countries)
].set_index("Country")[years].T

# Create the chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each country
for country in chart_data.columns:
    ax.plot(
        years,
        chart_data[country],
        marker="o",
        label=country
    )

# Formatting
ax.set_title(
    "Uzbekistan's Export Shares to Major Partners, 2015–2025",
    fontsize=16
)

ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Share of Total Exports (%)", fontsize=12)

ax.legend(
    title="Export Partner",
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    fontsize=9
)

plt.xticks(rotation=45)

plt.tight_layout()

# Save the chart
plt.savefig(
    "charts/export_partner_structure_2015_2025.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Compare major export partners between 2015 and 2025

comparison = shares[
    shares["Country"].isin(top_countries)
][["Country", "2015", "2025"]].copy()

comparison = comparison.sort_values(
    "2025",
    ascending=False
)

print("\nMajor export partners: 2015 vs 2025:")
print(comparison.to_string(index=False))

# Save the 2015 vs 2025 comparison
comparison.to_csv(
    "data/processed/export_partner_changes_2015_2025.csv",
    index=False
)

print("/nPartner comparison saved successfully.")

