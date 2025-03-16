# 🧠 Streamlit Chatbot using LangChain and Ollama

This project is a simple yet powerful chatbot interface built using [Streamlit](https://streamlit.io/), leveraging [LangChain](https://www.langchain.com/) and the [Ollama](https://ollama.com/) model `llama3.2:latest` for generating responses. The chatbot maintains conversation history and simulates an interactive assistant experience.

## 🚀 Features

- 💬 Chat interface with user and AI message display
- 📜 Conversation memory using `st.session_state`
- 🔗 Integrated with LangChain and Ollama's LLM API
- 🌡️ Adjustable temperature for model creativity (currently set to 3)


## 📦 Requirements

- Python 3.8+
- Streamlit
- LangChain Core
- LangChain Ollama



## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/streamlit-chatbot-ollama.git
   cd streamlit-chatbot-ollama
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:
   ```
   streamlit
   langchain-core
   langchain-ollama
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 📝 Code Overview

- `st.session_state.messages`: Stores the conversation history (HumanMessage and AIMessage).
- `ChatOllama`: Initializes the LLM model with temperature control.
- `st.chat_message`: Displays chat messages with respective roles (user or assistant).
- `st.chat_input`: Input box for users to send prompts.

---

## ⚙️ Configuration

- **Model Name**: `llama3.2:latest`  
- **Temperature**: `3` (Increase for more creativity, decrease for precision)

Modify this in:
```python
st.session_state.llm = ChatOllama(
    model = "llama3.2:latest",
    temperature=3
)
```

---

## 📸 Screenshot
![image](https://github.com/user-attachments/assets/58c3787f-5075-4e89-ae2c-2ab6d861d854)



---

## 🧩 Future Enhancements

- Support for multiple models via dropdown
- Model temperature control via sidebar
- File upload and context-based QA
- Memory persistence beyond session

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
