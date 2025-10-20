# main.py
import json
from agent import SupportAgent

def main():
    agent = SupportAgent()

    with open("tickets/sample_tickets.json", "r") as f:
        tickets = json.load(f)

    for ticket in tickets:
        print("\n============================")
        result = agent.handle_ticket(ticket)
        print("============================")
        print("Final Result:")
        print(result)

if __name__ == "__main__":
    main()
