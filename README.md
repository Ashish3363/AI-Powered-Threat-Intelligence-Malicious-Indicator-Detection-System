#  AI-Powered Threat Intelligence & Malicious Indicator Detection System

---

##  Project Description

This project is an **AI-based cybersecurity system** that detects whether a given IP address or URL is **malicious or safe** using machine learning.

It collects threat intelligence data from multiple sources like:

* AbuseIPDB
* URLHaus

The system:

1. Aggregates raw threat data
2. Cleans and normalizes inconsistent formats
3. Performs feature engineering
4. Trains a machine learning model
5. Predicts whether an indicator is malicious

---

##  Objective

Build a real-world AI system that can analyze threat indicators (IP/URL) and classify them as **malicious or benign**.

---

##  Tech Stack

* Python
* Pandas (Data Processing)
* Scikit-learn (ML Model)
* Random Forest Classifier
* Regex (Feature Extraction)

---

##  Project Structure

```
CyberSecurity+AI/
│
├── one.py                  # Fetch data from AbuseIPDB API
├── data_process.py         # Clean + normalize + feature engineering
├── model.py                # Train ML model
├── final_dataset.csv       # Processed dataset
├── cleaned_urlhaus.csv     # Cleaned URLHaus dataset
├── abuseipdb_data.csv      # Raw AbuseIPDB data
└── README.md               # Project documentation
```

---

##  Project Workflow

### 1️⃣ Data Collection

* Fetch IP threat data using AbuseIPDB API
* Download malware URLs dataset from URLHaus

---

### 2️⃣ Data Cleaning & Normalization

Different sources have different formats:

| Source    | Format    |
| --------- | --------- |
| AbuseIPDB | IP-based  |
| URLHaus   | URL-based |

Converted into a common schema:

```
indicator | type | confidence_score | report_count | country | source | timestamp
```

---

### 3️⃣ Feature Engineering (CORE)

Features created:

* indicator_length → length of URL/IP
* has_ip_pattern → detects IP inside URL
* special_char_count → suspicious characters
* days_since_seen → recency of threat
* frequency → repetition of indicator
* has_port → presence of port
* path_depth → URL complexity
* has_suspicious_word → phishing indicators

---

### 4️⃣ Data Leakage Handling

Initially, the model used `confidence_score`, which caused **data leakage**.

Fix:

* Removed confidence_score from training features

---

### 5️⃣ Model Training

* Algorithm: Random Forest Classifier
* Handles non-linear patterns and feature importance

---

### 6️⃣ Class Imbalance Handling

* Balanced dataset using sampling
* Used:

```
class_weight="balanced"
```

---

### 7️⃣ Model Evaluation

Metrics used:

* Precision
* Recall
* F1-score
* Accuracy

---

##  Architecture

```
        External Sources
     (AbuseIPDB, URLHaus)
                │
                ▼
        Data Collection (one.py)
                │
                ▼
        Data Processing (data_process.py)
        - Cleaning
        - Normalization
        - Feature Engineering
                │
                ▼
        Final Dataset (final_dataset.csv)
                │
                ▼
        ML Model (model.py)
        Random Forest Classifier
                │
                ▼
        Prediction Output
        (Malicious / Safe)
```

---

## ▶ How to Run the Project

### 🔹 Step 1: Clone Repository

```
git clone https://github.com/your-username/project-name.git
cd project-name
```

---

### 🔹 Step 2: Install Dependencies

```
pip install pandas scikit-learn numpy
```

---

### 🔹 Step 3: Collect Data

```
python one.py
```

---

### 🔹 Step 4: Process Data

```
python data_process.py
```

---

### 🔹 Step 5: Train Model

```
python model.py
```

---

##  Sample Output

```
precision    recall    f1-score

0   0.70      0.65      0.67
1   0.78      0.82      0.80

accuracy ≈ 0.75
```

---

##  Challenges Faced

* Data inconsistency across sources
* Missing fields (ISP, country)
* Data leakage issue
* Class imbalance problem
* Weak feature representation

---

##  Solutions Implemented

* Data normalization
* Feature engineering
* Removed leakage-causing features
* Balanced dataset
* Added domain-specific features

---

##  Future Improvements

* Use XGBoost / LightGBM
* Add GeoIP lookup
* Real-time detection API (FastAPI)
* Integrate with frontend (React dashboard)
* Deep learning for URL classification

---

##  Why This Project is Strong

* Uses real-world cybersecurity data
* Handles data leakage (advanced concept)
* Includes feature engineering
* Handles imbalance
* Mimics real threat intelligence systems

---

## 🧠 Short Description

AI-based cybersecurity system that detects malicious IPs and URLs using threat intelligence feeds, feature engineering, and machine learning.
