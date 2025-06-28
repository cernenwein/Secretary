import os
import json
import datetime
from flask import Flask, request, jsonify
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SECRETS_DIR = "/shared_memory/secrets"
CREDENTIALS_FILE = os.path.join(SECRETS_DIR, "credentials.json")
TOKEN_FILE = os.path.join(SECRETS_DIR, "token.json")

ALLOWED_CALENDAR_IDS = []  # Add allowed calendar IDs here
SCOPES = ["https://www.googleapis.com/auth/calendar"]

app = Flask(__name__)

def authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=8080)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return creds

creds = authenticate()
calendar_service = build("calendar", "v3", credentials=creds)

@app.route("/create_event", methods=["POST"])
def create_event():
    data = request.json
    summary = data.get("summary")
    start = data.get("start")
    end = data.get("end")
    description = data.get("description", "")
    calendar_id = ALLOWED_CALENDAR_IDS[0] if ALLOWED_CALENDAR_IDS else "primary"
    event = {
        "summary": summary,
        "start": {"dateTime": start, "timeZone": "UTC"},
        "end": {"dateTime": end, "timeZone": "UTC"},
        "description": description
    }
    created = calendar_service.events().insert(calendarId=calendar_id, body=event).execute()
    return jsonify({"status": "created", "id": created["id"]})

@app.route("/get_events", methods=["GET"])
def get_events():
    start = request.args.get("start")
    end = request.args.get("end")
    calendar_id = ALLOWED_CALENDAR_IDS[0] if ALLOWED_CALENDAR_IDS else "primary"
    events_result = calendar_service.events().list(
        calendarId=calendar_id, timeMin=start, timeMax=end,
        singleEvents=True, orderBy="startTime").execute()
    return jsonify(events_result.get("items", []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
