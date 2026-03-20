import pandas as pd

# Load raw file and REMOVE comment lines properly
df = pd.read_csv("urlhaus.csv", comment='#', header=None)

# Remove empty rows
df = df.dropna()

# Remove outer quotes
df[0] = df[0].str.strip('"')

# Split into columns
df = df[0].str.split('","', expand=True)

# Rename columns
df.columns = [
    "id",
    "date_added",
    "url",
    "status",
    "last_online",
    "threat",
    "tags",
    "urlhaus_link",
    "reporter"
]

# Remove any remaining invalid rows
df = df[df["url"].notna()]

print(df.head())

# Save clean dataset
df.to_csv("cleaned_urlhaus.csv", index=False)