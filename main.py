from monitoring import get_system_metrics
from detection import create_baseline, load_baseline
from alert import generate_alert
baseline = load_baseline()

metrics = get_system_metrics()

if baseline is None:
    print("Baseline not found. Creating baseline...")
    create_baseline(metrics)
else:
    print("Baseline already exists.")

import time
from monitoring import get_system_metrics
from detection import create_baseline, load_baseline, detect_anomaly

baseline = load_baseline()

if baseline is None:
    print("Baseline not found. Creating baseline...")
    metrics = get_system_metrics()
    create_baseline(metrics)
    baseline = load_baseline()

while True:
    metrics = get_system_metrics()

    print(f"CPU: {metrics['cpu']}% | Memory: {metrics['memory']}%")

    alert = detect_anomaly(metrics, baseline)

    if alert:
        print("⚠ ALERT:", alert)
    else:
        print("System Normal")   

    if alert:
        generate_alert(alert)
    else:
        print("System Normal")    

    time.sleep(5)