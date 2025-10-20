# tools/kb_retriever.py
kb = {
    "reset password": "To reset your password, click 'Forgot Password' on the login page. "
                      "Check your spam folder if you don't receive the email.",
    "invoice": "Invoices are available under Billing → Invoices. "
               "If missing, please contact accounts@company.com."
}

def retrieve_kb_article(query):
    for k, v in kb.items():
        if k in query:
            print(f"[KB] Found article for: {k}")
            return v
    print("[KB] No article found.")
    return None
