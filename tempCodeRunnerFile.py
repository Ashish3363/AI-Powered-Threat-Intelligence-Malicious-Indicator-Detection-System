

# Load AbuseIPDB data
abuse_df = pd.read_csv("abuseipdb_data.csv")

# Load URLHaus cleaned data
urlhaus_df = pd.read_csv("cleaned_urlhaus.csv")

print("===== AbuseIPDB Data =====")
print(abuse_df.head())
print("\nColumns:", abuse_df.columns)

print("\n===== URLHaus Data =====")
print(urlhaus_df.head())
print("\nColumns:", urlhaus_df.columns)