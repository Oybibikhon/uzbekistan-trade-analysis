import pandas as pd
# Load the raw trade data
input_file = "data/raw/trade _macro_2015_2025.csv" 
output_file = "data/processed/trade_indicators_2015_2025.csv"

df = pd.read_csv(input_file)

# Calculate trade indicators
df["Trade_Turnover_USD_million"] = ( 
    df["Exports_USD_million"] + df["Imports_USD_million"] 
    )
df["Trade_Balance_USD_million"] = ( 
    df["Exports_USD_million"] - df["Imports_USD_million"] 
    )
df["Trade_Openness_percent"] = ( 
    (df["Exports_USD_million"] + df["Imports_USD_million"]) 
    / df["GDP_USD_million"] 
    * 100 
    )
df["Export_Growth_percent"] = ( 
    df["Exports_USD_million"].pct_change() * 100 
    )
df["Import_Growth_percent"] = ( 
    df["Imports_USD_million"].pct_change() * 100 
    )
# Round calculated indicators for readability
df = df.round(2)
# Save the processed dataset
df.to_csv(output_file, index=False)
print("Processed dataset created successfully!") 
print(df)