# 🤖 Tool-Using Agent for Automatic Ticket Triage & Resolution (Agentic AI)

### 🧠 Overview
This project implements an **autonomous AI Agent** that automatically triages and resolves customer support tickets using multiple mock tools — just like an enterprise-level *Agentic AI* system would.  

It follows a **Plan → Act → Reflect loop**, parsing each ticket, deciding what actions to take, using tools such as KB Retriever or Config API, and either resolving or escalating the issue.  

This project was developed as part of the **AI Developer Assignment** for **DotKonnekt**.

---

## 🧩 Problem Statement
Support teams receive hundreds of repetitive tickets daily — *password resets, billing issues, plan upgrades*, etc.  
This project automates such repetitive cases intelligently by:
- Parsing incoming tickets (`title + description`)
- Planning which tools to use
- Calling mock APIs or retrieving KB articles
- Drafting appropriate replies
- Escalating complex or unknown issues

---

## ⚙️ System Design

### 🧱 Architecture
Customer Ticket → AI Agent (Plan → Act → Reflect) → Tool Calls → Reply / Escalation

yaml
Copy code

### 🧰 Tools Used

| Tool | Purpose |
|------|----------|
| **KB Retriever** | Fetches knowledge base article (mocked FAQ or small vector index) |
| **Config API** | Reads/writes simple user settings (mock of real backend API) |
| **Email API** | Drafts a customer-friendly email reply |
| **Escalation Logger** | Logs unresolved or unknown tickets for human review |

---

## 📂 Folder Structure
ai-ticket-agent/
│
├── agent.py # Core agent logic (Plan-Act-Reflect)
├── main.py # Entry script to execute the agent
├── tools/ # Mock tools for simulation
│ ├── kb_retriever.py
│ ├── config_api.py
│ ├── email_api.py
│ └── escalation_logger.py
├── tickets/ # Sample test tickets
│ └── sample_tickets.json
├── tests/ # Unit test scripts
│ └── test_agent.py
├── requirements.txt
├── README.md
└── escalations.log # Auto-generated log of escalated tickets

yaml
Copy code

---

## 💻 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/ai-ticket-agent.git
cd ai-ticket-agent
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the project
bash
Copy code
python main.py
4️⃣ (Optional) Run automated tests
bash
Copy code
pytest
🧪 Example Run
🎫 Input Ticket
json
Copy code
{
  "title": "Password Reset Issue",
  "description": "I tried resetting my password but didn’t get any link."
}
🤖 Agent Process
Parses ticket → detects “password” intent

Calls KB Retriever → fetches article on password reset

Calls Email API → drafts reply message

Returns reply and action logs

✅ Output
json
Copy code
{
  "status": "resolved",
  "reply": "Subject: Password Reset Issue\n\nDear user,\nTo reset your password, click 'Forgot Password' on the login page. Check your spam folder if you don't receive the email.\n\nRegards,\nSupport Team",
  "logs": [
    "Intent identified: Password Reset",
    "KB article retrieved successfully."
  ]
}
If the issue is unknown or cannot be solved, it automatically escalates:

json
Copy code
{
  "status": "escalated",
  "reason": "Unknown issue type",
  "logs": [
    "Escalated: Unknown issue type"
  ]
}
🧰 Tools Explained
🔹 KB Retriever (tools/kb_retriever.py)
Fetches a predefined KB response.
In a production version, this would connect to a RAG (Retrieval-Augmented Generation) system such as FAISS or Chroma to search across large company documents.

🔹 Config API (tools/config_api.py)
Simulates user configuration read/write operations.
In a real scenario, this connects to backend APIs or databases (e.g., account plans, billing details).

🔹 Email API (tools/email_api.py)
Drafts polite and context-aware replies.
In production, this would use services like SendGrid, Gmail API, or AWS SES to send actual emails.

🔹 Escalation Logger (tools/escalation_logger.py)
Logs unsolved tickets with concise summaries for human review.
In an enterprise setup, this would create tickets in Jira, Zendesk, or ServiceNow.

🏭 Real-World Use Case
Example Ticket	Real-world Agent Action
“Reset my password but I can’t find the link.”	Retrieves KB → sends password reset email automatically
“Upgrade plan to Pro monthly.”	Reads current plan → updates config via API → drafts confirmation reply
“Invoice missing for August.”	Searches KB → if missing, escalates to human with summary
“Server configuration failed.”	Escalates immediately with suspected root cause

🚀 Future Enhancements
🔹 Integrate RAG-based retriever from Task 1 for true document-based knowledge retrieval

🔹 Connect to real REST APIs for password reset, billing, and plan updates

🔹 Add Streamlit web UI for interactive ticket submission

🔹 Add authentication & confirmation flows for write operations

🔹 Implement Dockerfile for easy deployment

🔹 Maintain a MongoDB / SQLite log for audit and analytics

🧩 Tech Stack
Language: Python 3.9+

Libraries: pytest, streamlit (optional for UI)

Architecture: Modular, tool-based agent with Plan–Act–Reflect loop

Style: Simple, explainable, and extendable for real-world enterprise use

📦 Installation & Run Summary
bash
Copy code
# Clone project
git clone https://github.com/ajaykumar057/ai_ticket_agent.git

# Navigate
cd ai-ticket-agent

# Install dependencies
pip install -r requirements.txt

# Run agent
python main.py

# Run tests
pytest

🧠 Industry Relevance
This project simulates how real AI support assistants (used by SaaS companies, telecoms, or e-commerce) handle support tickets automatically.
In real-world deployment, such systems connect to:

Customer databases

Email automation systems

Knowledge management systems

Ticketing platforms

Your project demonstrates the core decision-making and automation logic — the “brain” — that can later integrate with those systems.

👨‍💻 Author
Ajay Kumar
AI Developer Assignment – DotKonnekt


“Building intelligent agents that think, plan, and act like real support engineers.”
