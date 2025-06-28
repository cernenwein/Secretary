import os
import json
import time
from datetime import datetime
from twilio.rest import Client

SECRETS_FILE = "/shared_memory/secrets/twilio.json"
REMINDERS_FILE = "/shared_memory/reminders.json"
SENT_LOG = "/shared_memory/sent_reminders_log.json"

def now():
    return datetime.utcnow().isoformat() + "Z"

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def send_sms(task, config):
    client = Client(config["account_sid"], config["auth_token"])
    message = client.messages.create(
        body=f"📝 Reminder: {task}",
        from_=config["from_number"],
        to=config["to_number"]
    )
    print(f"📤 Sent SMS: {message.sid}")

def main():
    print("📲 SMS Notifier running (hourly)...")
    while True:
        config = load_json(SECRETS_FILE, {})
        if not config:
            print("❌ Twilio credentials not found.")
            time.sleep(3600)
            continue

        reminders = load_json(REMINDERS_FILE, {"tasks": []})
        sent_log = load_json(SENT_LOG, {})

        for task in reminders["tasks"]:
            task_text = task["task"]
            if task_text not in sent_log:
                try:
                    send_sms(task_text, config)
                    sent_log[task_text] = now()
                except Exception as e:
                    print(f"⚠️ Failed to send SMS: {e}")

        save_json(SENT_LOG, sent_log)
        time.sleep(3600)

if __name__ == "__main__":
    main()
