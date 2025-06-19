from plyer import notification
import psutil

def alert_user(message):
    notification.notify(
        title="Ransomware Alert 🚨",
        message=message,
        timeout=5
    )

def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        print(f"[ALERT] Terminated suspicious process with PID: {pid}")
    except Exception as e:
        print(f"[ERROR] Could not kill process: {e}")
