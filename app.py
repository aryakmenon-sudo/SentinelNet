from flask import Flask, render_template
from monitoring import get_system_metrics
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():

    metrics = get_system_metrics()

    cpu = metrics["cpu"]
    memory = metrics["memory"]

    # STATUS
    if cpu > 50:
        status = "ALERT"
        status_class = "alert"
        last_alert = "High CPU Usage Detected"
    else:
        status = "Healthy"
        status_class = "normal"
        last_alert = "None"

    # TIME ENTRY
    current_time = datetime.now().strftime("%H:%M")

    new_entry = {
        "time": current_time,
        "cpu": cpu,
        "memory": memory
    }

    # LOAD OLD DATA
    try:
        with open("metrics.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    # ADD NEW DATA
    data.append(new_entry)

    # KEEP ONLY LAST 50
    data = data[-50:]

    # SAVE
    with open("metrics.json", "w") as file:
        json.dump(data, file)

    # GRAPH VARIABLES
    times = [entry["time"] for entry in data]
    cpu_values = [entry["cpu"] for entry in data]
    memory_values = [entry["memory"] for entry in data]

    return render_template(
        "dashboard.html",
        cpu=cpu,
        memory=memory,
        status=status,
        status_class=status_class,
        last_alert=last_alert,
        times=times,
        cpu_values=cpu_values,
        memory_values=memory_values
   )
@app.route("/history-page")

def history_page():

    try:
        with open("alerts.log", "r") as file:
            alerts = file.readlines()
    except:
        alerts = []

    alerts.reverse()

    return render_template(
        "history.html",
        alerts=alerts
    )
@app.route("/history")
def history():

    try:
        with open("metrics.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    return data

if __name__ == "__main__":
    app.run(debug=True)