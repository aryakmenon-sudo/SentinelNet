import datetime
from plyer import notification

LOG_FILE = "alerts.log"
MAX_ALERTS = 30

def generate_alert(message):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    alert_message = f"[{timestamp}] ALERT: {message}"

    print(alert_message)

    # READ OLD ALERTS
    try:
        with open(LOG_FILE, "r") as file:
            alerts = file.readlines()
    except:
        alerts = []

    # ADD NEW ALERT
    alerts.append(alert_message + "\n")

    # KEEP ONLY LAST 30
    alerts = alerts[-MAX_ALERTS:]

    # SAVE AGAIN
    with open(LOG_FILE, "w") as file:
        file.writelines(alerts)

    # POPUP
    notification.notify(
        title="Sentinel Net Alert 🚨",
        message=message,
        timeout=5
    )