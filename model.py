# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report

# # Load dataset
# df = pd.read_csv("final_dataset.csv")

# # Create balanced dataset manually
# malicious_df = df.copy()
# malicious_df["label"] = 1

# # Create pseudo-safe data (but NOT too obvious)
# safe_df = df.sample(frac=0.5, random_state=42).copy()
# safe_df["confidence_score"] = safe_df["confidence_score"] * 0.3  # reduce, not zero
# safe_df["label"] = 0

# # Combine both
# df = pd.concat([malicious_df, safe_df])

# # Balance dataset
# df = df.sample(frac=1, random_state=42)  # shuffle

# print(df["label"].value_counts())

# # -----------------------------
# # STEP 2: Prepare Features
# # -----------------------------
# # Convert type to numeric
# df["type"] = df["type"].map({"IP": 0, "URL": 1})

# # Select features
# # X = df[[
# #     "confidence_score",
# #     "report_count",
# #     "days_since_seen",
# #     "frequency",
# #     "type"
# # ]]

# X = df[[
#     "confidence_score",
#     "report_count",
#     "days_since_seen",
#     "frequency",
#     "type",
#     "indicator_length",
#     "has_ip_pattern",
#     "special_char_count"
# ]]

# y = df["label"]

# # Handle missing values
# X = X.fillna(0)


# # -----------------------------
# # STEP 3: Train/Test Split
# # -----------------------------
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # -----------------------------
# # STEP 4: Train Model
# # -----------------------------
# model = RandomForestClassifier(
#     n_estimators=200,
#     max_depth=10,
#     min_samples_split=5,
#     random_state=42
# )

# model.fit(X_train, y_train)

# # -----------------------------
# # STEP 5: Evaluate
# # -----------------------------
# y_pred = model.predict(X_test)

# print("\nClassification Report:")
# print(classification_report(y_test, y_pred))




import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("final_dataset.csv")

# Malicious data
malicious_df = df.copy()
malicious_df["label"] = 1
malicious_df["confidence_score"] = malicious_df["confidence_score"] + np.random.randint(-10, 10, size=len(malicious_df))

# Safe data
safe_df = df.sample(frac=0.5, random_state=42).copy()
safe_df["confidence_score"] = np.random.uniform(10, 60, size=len(safe_df))
safe_df["label"] = 0

# Combine
# Balance both classes
min_size = min(len(malicious_df), len(safe_df))

malicious_df = malicious_df.sample(n=min_size, random_state=42)
safe_df = safe_df.sample(n=min_size, random_state=42)

df = pd.concat([malicious_df, safe_df])

# Shuffle
df = df.sample(frac=1, random_state=42)

print(df["label"].value_counts())

# Convert type
df["type"] = df["type"].map({"IP": 0, "URL": 1})

# Features (NO confidence_score ❌)
X = df[[
    "report_count",
    "days_since_seen",
    "frequency",
    "type",
    "indicator_length",
    "has_ip_pattern",
    "special_char_count"
]]

y = df["label"]

X = X.fillna(0)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight="balanced", 
    min_samples_split=5,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\nPrediction Distribution:")
print(pd.Series(y_pred).value_counts())

print("\nClassification Report:")
print(classification_report(y_test, y_pred))