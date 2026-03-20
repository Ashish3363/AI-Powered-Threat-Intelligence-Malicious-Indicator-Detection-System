import numpy as np
import re

def add_basic_features(df):
    # Length of indicator
    df["indicator_length"] = df["indicator"].astype(str).apply(len)

    # Check if IP pattern exists
    df["has_ip_pattern"] = df["indicator"].str.contains(r'\d+\.\d+\.\d+\.\d+', regex=True).astype(int)

    # Count special characters
    df["special_char_count"] = df["indicator"].str.count(r'[^a-zA-Z0-9]')

    return df


def add_url_features(df):
    # Port detection
    df["has_port"] = df["indicator"].str.contains(r':\d+', regex=True).astype(int)

    # Path depth
    df["path_depth"] = df["indicator"].str.count('/')

    # Suspicious keywords
    suspicious_words = ["login", "secure", "bank", "verify", "update"]

    def check_keywords(x):
        return int(any(word in str(x).lower() for word in suspicious_words))

    df["has_suspicious_word"] = df["indicator"].apply(check_keywords)

    return df


def add_telemetry_features(df):
    # Simulated telemetry
    df["failed_login_count"] = np.random.randint(0, 50, len(df))
    df["request_rate"] = np.random.randint(1, 500, len(df))
    df["unique_ports"] = np.random.randint(1, 10, len(df))

    # Behavioral signals
    df["is_brute_force"] = (df["failed_login_count"] > 20).astype(int)
    df["is_port_scan"] = (df["unique_ports"] > 5).astype(int)

    return df


def summarize(df):
    df = add_basic_features(df)
    df = add_url_features(df)
    df = add_telemetry_features(df)
    return df