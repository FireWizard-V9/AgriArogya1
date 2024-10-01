import streamlit as st
import chatbot_backend as demo  # Import your chatbot backend file as demo

def app():
    # Set title for the chatbot
    st.title("CropTalk 😎")  # Customize this title as needed

    # Initialize memory for the conversation in session state
    if 'memory' not in st.session_state:
        st.session_state.memory = demo.demo_memory()  # Initialize memory

    # Initialize chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []  # Initialize chat history

    # Re-render the chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["text"])

    # Get user input from the chat input box
    input_text = st.chat_input("From Seeds to Harvest! i am here to cultivate success")  # Placeholder text for the chat input box

    if input_text:  # If the user provides input
        with st.chat_message("user"):
            st.markdown(input_text)

        # Add user input to chat history
        st.session_state.chat_history.append({"role": "user", "text": input_text})

        # Get chatbot response
        try:
            chat_response = demo.demo_conversation(input_text=input_text, memory=st.session_state.memory)
            
            # Ensure the chatbot response is in string format
            if not isinstance(chat_response, str):
                chat_response = str(chat_response)

            # Display chatbot response
            with st.chat_message("assistant"):
                st.markdown(chat_response)

            # Add chatbot response to chat history
            st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
        except Exception as e:
            st.error(f"Error: {e}")  # Display error message if something goes wrong
