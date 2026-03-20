import pandas as pd
from summarizer import summarize
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

abuse_normalized = pd.DataFrame()

abuse_normalized["indicator"] = abuse_df["indicator"]
abuse_normalized["type"] = "IP"
abuse_normalized["confidence_score"] = abuse_df["confidence_score"]
abuse_normalized["report_count"] = 0
abuse_normalized["country"] = abuse_df["country"]
abuse_normalized["source"] = "AbuseIPDB"
abuse_normalized["timestamp"] = abuse_df["last_reported"]

print("\nAbuse Normalized:")
print(abuse_normalized.head())

urlhaus_normalized = pd.DataFrame()

urlhaus_normalized["indicator"] = urlhaus_df["url"]
urlhaus_normalized["type"] = "URL"
urlhaus_normalized["confidence_score"] = 80   # assumed malicious
urlhaus_normalized["report_count"] = 1
urlhaus_normalized["country"] = "Unknown"
urlhaus_normalized["source"] = "URLHaus"
urlhaus_normalized["timestamp"] = urlhaus_df["date_added"]

print("\nURLHaus Normalized:")
print(urlhaus_normalized.head())


final_df = pd.concat([abuse_normalized, urlhaus_normalized])

print("\nFinal Combined Data:")
print(final_df.head())

# Save final dataset
# final_df.to_csv("final_dataset.csv", index=False)

# Convert timestamp
final_df["timestamp"] = pd.to_datetime(final_df["timestamp"], errors='coerce', utc=True)

# Recency feature
final_df["days_since_seen"] = (pd.Timestamp.now(tz='UTC') - final_df["timestamp"]).dt.days

# Frequency feature
final_df["frequency"] = final_df.groupby("indicator")["indicator"].transform("count")

# Label (all malicious for now)
final_df["label"] = 1

# Length of indicator (URL/IP)
final_df["indicator_length"] = final_df["indicator"].astype(str).apply(len)

# Check if indicator contains IP pattern
final_df["has_ip_pattern"] = final_df["indicator"].str.contains(r'\d+\.\d+\.\d+\.\d+', regex=True).astype(int)

# Count special characters (URLs with many symbols are suspicious)
final_df["special_char_count"] = final_df["indicator"].str.count(r'[^a-zA-Z0-9]')

print("\nFinal with Features:")
print(final_df.head())

final_df = summarize(final_df)
# Save AFTER feature engineering
final_df.to_csv("final_dataset.csv", index=False)