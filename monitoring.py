import psutil
import time

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    processes = []
    for process in psutil.process_iter(['name']):
        try:
            processes.append(process.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return {
        "cpu": cpu_usage,
        "memory": memory_usage,
        "processes": processes
    }


if __name__ == "__main__":
    while True:
        metrics = get_system_metrics()
        
        print("\n=== SYSTEM STATUS ===")
        print(f"CPU Usage: {metrics['cpu']}%")
        print(f"Memory Usage: {metrics['memory']}%")
        print(f"Running Processes Count: {len(metrics['processes'])}")
        
        time.sleep(5)