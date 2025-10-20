import streamlit as st
from agent import SupportAgent

st.title("🧠 AI Support Agent")
st.write("Submit your support ticket below:")

title = st.text_input("Ticket Title")
desc = st.text_area("Ticket Description")

if st.button("Submit Ticket"):
    agent = SupportAgent()
    ticket = {"title": title, "description": desc}
    result = agent.handle_ticket(ticket)
    st.json(result)
