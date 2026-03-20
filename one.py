import requests
import pandas as pd

API_KEY = "b70df383dcca38602ed6f4b5a3c02d0c076bf683cca0929325cea6b265fea35eba79cc3f0be4f9aa"

url = "https://api.abuseipdb.com/api/v2/blacklist"

headers = {
    "Key": API_KEY,
    "Accept": "application/json"
}

params = {
    "confidenceMinimum": 50  # only high-risk IPs
}

response = requests.get(url, headers=headers, params=params)

data = response.json()

# Extract useful data
records = []

for item in data["data"]:
    records.append({
        "indicator": item.get("ipAddress"),
        "confidence_score": item.get("abuseConfidenceScore", 0),
        "country": item.get("countryCode", "Unknown"),
        "isp": item.get("isp", "Unknown"),
        "last_reported": item.get("lastReportedAt")
    })
df = pd.DataFrame(records)

print(df.head())

# Save dataset
df.to_csv("abuseipdb_data.csv", index=False)