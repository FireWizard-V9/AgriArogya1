import streamlit as st
from PIL import Image

# Set page title and header as the first Streamlit command
st.set_page_config(page_title="AgriAarogya - Predictive Crop Disease Model", layout="wide")

# Define the app function
def app():
    # Load images (make sure the paths are correct)
    crop_disease_image = Image.open(r'C:\Users\sahil\OneDrive\Documents\AgriArogya\bg1.jpeg')
    ai_assistant_image = Image.open(r'C:\Users\sahil\OneDrive\Documents\AgriArogya\6.jpeg')
    insights_image = Image.open(r'C:\Users\sahil\OneDrive\Documents\AgriArogya\2.jpeg')
    recommendations_image = Image.open(r'C:\Users\sahil\OneDrive\Documents\AgriArogya\5.jpeg')

    # Set page title and header
    st.title("🌾 AgriArogya 🌿")
    st.header("Empowering Farmers with Predictive Insights for Healthier Crops")

    # Model description
    st.write("""
    **AgriAarogya** is a cutting-edge predictive model that utilizes machine learning to forecast crop diseases by analyzing weather, soil, and historical data. By providing early warnings, AgriAarogya helps farmers reduce losses and boost productivity.
    """)

    # Key Features section
    st.subheader("Key Features")
    col1, col2 = st.columns(2)

    with col1:
        st.image(crop_disease_image, caption='Early Detection of Widespread Crop Diseases', use_column_width=True)
        st.markdown("""
        <h4 style='font-size:22px;'>Early Detection of Widespread Crop Diseases</h4>
        <p style='font-size:18px;'>Identifies potential disease outbreaks early using machine learning, helping prevent crop damage.</p>
        """, unsafe_allow_html=True)

    with col2:
        st.image(ai_assistant_image, caption='24/7 AI Assistant Agribot Facility', use_column_width=True)
        st.markdown("""
        <h4 style='font-size:22px;'>24/7 AI Assistant Agribot Facility</h4>
        <p style='font-size:18px;'>Provides round-the-clock support and advice on crop management and issues through an AI assistant.</p>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.image(insights_image, caption='Valuable Insights via Q&A', use_column_width=True)
        st.markdown("""
        <h4 style='font-size:22px;'>Valuable Insights via Q&A</h4>
        <p style='font-size:18px;'>Delivers data-driven answers to specific agricultural questions, aiding informed decision-making.</p>
        """, unsafe_allow_html=True)

    with col4:
        st.image(recommendations_image, caption='Personalized Crop Recommendations', use_column_width=True)
        st.markdown("""
        <h4 style='font-size:22px;'>Personalized Crop Recommendations</h4>
        <p style='font-size:18px;'>Offers tailored crop advice based on detailed farm data, optimizing choices for better yields.</p>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    ---
    *AgriAarogya - A step towards sustainable farming.*
    """)

