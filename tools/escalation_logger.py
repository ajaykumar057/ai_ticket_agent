# tools/escalation_logger.py
def log_escalation(ticket, reason):
    print(f"[Escalation] Logging issue: {reason}")
    with open("escalations.log", "a") as f:
        f.write(f"Escalated Ticket: {ticket['title']} | Reason: {reason}\n")
