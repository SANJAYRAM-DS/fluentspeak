from config.celery import app


@app.task
def summarize_conversation(conversation_id):
    return {"conversation_id": str(conversation_id), "status": "queued"}


@app.task
def track_event(user_id, event_name, payload=None):
    return {"user_id": str(user_id), "event_name": event_name, "payload": payload or {}}


@app.task
def send_reminder(user_id):
    return {"user_id": str(user_id), "status": "queued"}


@app.task
def check_provider_health():
    return {"status": "queued"}
