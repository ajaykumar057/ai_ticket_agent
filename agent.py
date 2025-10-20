# agent.py
from tools.kb_retriever import retrieve_kb_article
from tools.config_api import read_config, write_config
from tools.email_api import draft_reply
from tools.escalation_logger import log_escalation

class SupportAgent:
    def __init__(self):
        self.logs = []

    def handle_ticket(self, ticket):
        title = ticket.get("title", "").lower()
        desc = ticket.get("description", "").lower()
        self.logs = []

        print(f"\n[Agent] Handling Ticket: {title}")

        # Step 1: Parse and decide intent
        if "password" in desc:
            return self.reset_password_flow(ticket)
        elif "upgrade" in desc or "plan" in desc:
            return self.plan_upgrade_flow(ticket)
        elif "invoice" in desc or "bill" in desc:
            return self.invoice_issue_flow(ticket)
        else:
            return self.escalate(ticket, "Unknown issue type")

    # Flow 1: Password reset
    def reset_password_flow(self, ticket):
        self.logs.append("Intent identified: Password Reset")
        kb_article = retrieve_kb_article("reset password")

        if kb_article:
            reply = draft_reply(ticket["title"], kb_article)
            self.logs.append("KB article retrieved successfully.")
            return {"status": "resolved", "reply": reply, "logs": self.logs}
        else:
            return self.escalate(ticket, "KB article missing")

    # Flow 2: Plan upgrade
    def plan_upgrade_flow(self, ticket):
        self.logs.append("Intent identified: Plan Upgrade")
        plan = read_config("plan")

        if plan != "Pro":
            write_config("plan", "Pro")
            reply = draft_reply(ticket["title"], "Your plan has been successfully upgraded to Pro.")
            self.logs.append("Plan updated successfully.")
            return {"status": "resolved", "reply": reply, "logs": self.logs}
        else:
            return self.escalate(ticket, "Already on Pro plan")

    # Flow 3: Invoice Issue
    def invoice_issue_flow(self, ticket):
        self.logs.append("Intent identified: Invoice Issue")
        kb_article = retrieve_kb_article("invoice")

        if kb_article:
            reply = draft_reply(ticket["title"], kb_article)
            self.logs.append("Provided invoice instructions.")
            return {"status": "resolved", "reply": reply, "logs": self.logs}
        else:
            return self.escalate(ticket, "No invoice record found")

    # Escalation handling
    def escalate(self, ticket, reason):
        log_escalation(ticket, reason)
        self.logs.append(f"Escalated: {reason}")
        return {"status": "escalated", "reason": reason, "logs": self.logs}
