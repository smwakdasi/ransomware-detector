import pandas as pd
import os

def extract_features_from_logs(log_file_path):
    if not os.path.exists(log_file_path):
        print(f"[ERROR] Log file not found: {log_file_path}")
        return None

    df = pd.read_csv(log_file_path)

    features = {
        "file_modifications": df[df["event"] == "modified"].shape[0],
        "file_creations": df[df["event"] == "created"].shape[0],
        "file_deletions": df[df["event"] == "deleted"].shape[0]
    }

    return pd.DataFrame([features])
