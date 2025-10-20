# tools/email_api.py
def draft_reply(subject, message):
    print(f"[Email API] Drafting reply for: {subject}")
    return f"Subject: {subject}\n\nDear user,\n{message}\n\nRegards,\nSupport Team"
