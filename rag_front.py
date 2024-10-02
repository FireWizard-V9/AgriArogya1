import streamlit as st
import rag_back as demo  # Replace rag_back with your actual backend filename
from rag_back import hr_index

# Wrapping the logic inside an app function for modularity
def app():
    # Set the page title and description inside the app function
    new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">QNA with AgriBot 🎯</p>'
    st.markdown(new_title, unsafe_allow_html=True)  # Display the title with custom styling

    # Initialize vector index in session state, loading only if not already initialized
    if 'vector_index' not in st.session_state:
        with st.spinner("📀 Wait for magic... All beautiful things in life take time :-)"):  # Spinner message
            st.session_state.vector_index = demo.hr_index()  # Your Index Function from Backend

    # Input area for user query
    input_text = st.text_area("Input text", label_visibility="collapsed")

    # Button to process the query
    go_button = st.button("Harvest your Queries", type="primary")

    if go_button:
        if input_text.strip() == "":  # Check if input text is empty
            st.warning("Please enter a query before harvesting!")
        else:
            # Display a spinner while processing the response
            with st.spinner("📢 I will do Research on your behalf, meanwhile you can rest!!"):
                try:
                    # Get the response from the backend (RAG function)
                    response_content = demo.hr_rag_response(index=st.session_state.vector_index, question=input_text)
                    st.write(response_content)  # Display the response
                except Exception as e:
                    st.error(f"Something went wrong: {e}")  # Display error if something goes wrong

# No need to call app() here, it will be called from app.py
