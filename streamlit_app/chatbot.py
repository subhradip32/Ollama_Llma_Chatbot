import streamlit as st 
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama


st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "llm" not in st.session_state:
    st.session_state.llm = ChatOllama(
        model = "llama3.2:latest",
        temperature= 3
    )


for message in st.session_state.messages: 
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    if isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

prompt = st.chat_input("Say something")

if prompt: 
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append(HumanMessage(prompt))

    # response = f"Echo: {prompt}"
    response = st.session_state.llm.invoke(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.content)

        st.session_state.messages.append(AIMessage(response.content))
