import os

BASELINE_FILE = "baseline.txt"


def create_baseline(metrics):
    cpu = metrics["cpu"]
    memory = metrics["memory"]

    with open(BASELINE_FILE, "w") as file:
        file.write(f"{cpu},{memory}")

    print("Baseline saved successfully.")


def load_baseline():
    if not os.path.exists(BASELINE_FILE):
        return None

    with open(BASELINE_FILE, "r") as file:
        data = file.read().split(",")

    return {
        "cpu": float(data[0]),
        "memory": float(data[1])
    }
def detect_anomaly(metrics, baseline):
    cpu_threshold = baseline["cpu"] + 15
    memory_threshold = baseline["memory"] +15

    if metrics["cpu"] > cpu_threshold:
        return "High CPU Usage Detected"

    if metrics["memory"] > memory_threshold:
        return "High Memory Usage Detected"

    return None    
