import streamlit as st
from pathlib import Path
import home
import chatbot_frontend
import know
import dashboard
import crop_recomen
import yeild
import chatbot_backend
import rag_back
import rag_front

# Set page configuration (MUST be at the top)
st.set_page_config(page_title="AgriArogya", page_icon="🌱")

# Dictionary to map page names to functions with corresponding icons
PAGES = {
    "Home": {
        "module": home,
        "icon": "🏠"
    },
    "RAG Chatbot": {
        "module": rag_front,  # Changed from chatbot_frontend to rag_front for RAG chatbot
        "icon": "🤖"
    },
    "Croptalk": {
        "module": know,
        "icon": "🌾"
    },
    "Dashboard": {
        "module": dashboard,
        "icon": "📊"
    },
    "Crop Recommendation": {
        "module": crop_recomen,
        "icon": "🌱"
    },
    "Crop Yield Prediction": {
        "module": yeild,
        "icon": "📈"
    }
}

# Sidebar styling (Streamlit's built-in CSS customization)
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f5;
        padding: 10px;
    }
    .sidebar .sidebar-content .st-radio {
        color: black;
    }
    .sidebar .sidebar-title {
        font-size: 24px;
        color: #4CAF50;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)

# Custom Sidebar Navigation
st.sidebar.title("Navigation")
for page, info in PAGES.items():
    st.sidebar.write(f"{info['icon']} {page}")

selection = st.sidebar.radio(
    "Go to",
    list(PAGES.keys()),
    format_func=lambda page: f"{PAGES[page]['icon']} {page}"
)

# Display the selected page
page = PAGES[selection]["module"]
page.app()  # Calls the `app()` function of the selected page

# Main app title and sidebar notice
st.title("AgriArogya")
st.sidebar.success("Services")

# Footer style
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }
    .stApp {
        margin-bottom: 50px;
    }
    </style>
    """, unsafe_allow_html=True
)
