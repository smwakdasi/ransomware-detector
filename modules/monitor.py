import time
import psutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from modules.alert import alert_user, kill_process

class RansomwareBehaviorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"[MONITOR] File modified: {event.src_path}")

def monitor_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > 90:
        print("[WARNING] High CPU usage detected!")
        alert_user("High CPU usage — potential ransomware!")
        current_pid = os.getpid()
        kill_process(current_pid)

def start_monitoring():
    path = os.path.expanduser("~")  # Monitor user's home directory
    observer = Observer()
    observer.schedule(RansomwareBehaviorHandler(), path=path, recursive=True)
    observer.start()
    print("[MONITOR] Monitoring started... Press CTRL+C to stop.")
    try:
        while True:
            monitor_cpu()
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("[MONITOR] Monitoring stopped.")
    observer.join()
