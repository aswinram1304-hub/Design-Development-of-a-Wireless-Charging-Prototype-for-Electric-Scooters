import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Number of records
N = 1000

# Generate timestamps (e.g., 1 minute interval)
start = datetime(2025,2,1,8,0,0)
timestamps = [start + timedelta(minutes=i) for i in range(N)]

# Generate synthetic data
data = {
    "timestamp": timestamps,
    "scooter_id": np.random.choice([f"SCOOTER_{i}" for i in range(1,51)], N),
    "battery_soc": np.random.uniform(10, 100, N).round(1),
    "charging_power_w": np.random.normal(350, 50, N).clip(100, 600),
    "coil_alignment_mm": np.random.uniform(0, 50, N).round(1),
    "power_loss_pct": np.random.uniform(5, 20, N).round(1),
    "temp_c": np.random.uniform(15, 40, N).round(1),
    "charging_status": np.random.choice(["Active","Idle","Completed"], N, p=[0.6,0.2,0.2])
}

# Derived metric
data["energy_transferred_wh"] = \
    (data["charging_power_w"] * np.random.uniform(0.1, 1.0, N)).round(1)

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("wireless_charging_scooter_dataset.csv", index=False)

print("Dataset created with shape:", df.shape)
