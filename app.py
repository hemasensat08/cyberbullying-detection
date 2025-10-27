import streamlit as st
from textblob import TextBlob

# Admin email/alert placeholder
ADMIN = "admin@example.com"

st.title("Cyberbullying Detection Tool 🚨")

msg = st.text_input("Enter a message:")

if st.button("Check"):
    if msg:
        # Simple rule: check if sentiment is negative or contains bad words
        bullying_words = ["stupid", "idiot", "hate", "kill", "loser", "ugly"]
        if any(word in msg.lower() for word in bullying_words) or TextBlob(msg).sentiment.polarity < -0.3:
            st.error("⚠️ Bullying Message Detected! Admin Notified.")
            # Here you can add code to send email/DB alert
            st.write(f"Notification sent to {ADMIN}")
        else:
            st.success("✅ Message is safe.")
    else:
        st.warning("Please enter a message.")
