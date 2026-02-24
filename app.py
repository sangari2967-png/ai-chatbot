import streamlit as st
import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('punkt_tab') 
nltk.download('stopwords')

stop_words = set(stopwords.words("english"))

st.title("🤖 AI Chatbot with NLTK")

def bot_reply(text):
    tokens = word_tokenize(text.lower())
    words = [w for w in tokens if w not in stop_words]

    if any(word.startswith("hi") for word in words) or "hello" in words:
     return "Hello! Nice to meet you 😊"
    elif "how" in text.lower() or "you" in text.lower():
        return "I am fine 😄"
    elif "name" in words:
        return "I am your AI chatbot."
    elif "course" in words or "doubt" in words:
        return "Tell me your doubt, I’ll help you."
    elif "college" in words:
        return "Hope your college life is going great!"
    elif "time" in words:
        return datetime.datetime.now().strftime("Current time: %H:%M:%S")
    elif "joke" in words:
        return "Why did the computer go to doctor? Because it had a virus😄"
    elif "python" in words:
        return "Python is my native language! It's a great choice for AI."
    elif "love" in words:
        return "I'm a bot,but i have a high capacity had drive for our friendship."
    elif "bye" in words:
        return "Goodbye! Have a nice day 👋"
    else:
        return "Sorry, I didn't understand."

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = bot_reply(user_input)

    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
