import streamlit as st
from Home_Page import show_home
from Diabetes_Prediction_page import show_diabetes_prediction_page
from Heart_Attack_Prediction_page import show_heart_attack_prediction_page
from Lung_Cancer_Prediction_page import show_lung_cancer_prediction_page
from Explore_page import show_diabetes_explore_page, show_heart_attack_explore_page, show_lung_cancer_explore_page
from Info import show_info
from About_me_page import about_me
from chatbot import Chatbot

Chatbot()

st.set_page_config(
    page_title="Health Explorer(By Neev Sharma)",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar styling
st.markdown("""
<style>
/* Lock sidebar size ONLY when visible */
section[data-testid="stSidebar"][aria-expanded="true"] {
    width: 300px !important;
    min-width: 300px !important;
    max-width: 300px !important;
    color: black;
}
section[data-testid="stSidebar"][aria-expanded="false"] {
    width: 0 !important;
    color: black;
    min-width: 0 !important;
    max-width: 0 !important;
}
/* Sidebar background */
section[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #cce3f9 0%, #90caf9 50%, #64b5f6 100%);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Move background gradient of main container
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #3a7bd5, #00d2ff) !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar SELECT text
st.sidebar.markdown("<p style='color: black; font-weight: 600;'>SELECT</p>", unsafe_allow_html=True)

# Sidebar select box
sidebar = st.sidebar.selectbox(
    "",
    options=[
        "🏠 Home",
        "💉 Diabetes Predictor",
        "❤️ Heart Attack Predictor",
        "🫁 Lung Cancer Predictor",
        "📊 Explore",
        "🧾 Info",
        "👨‍💻 About Me"
    ],
    label_visibility="collapsed"
)

# Main page routing
if sidebar == '🏠 Home':
    show_home()
elif sidebar == '💉 Diabetes Predictor':
    show_diabetes_prediction_page()
elif sidebar == '❤️ Heart Attack Predictor':
    show_heart_attack_prediction_page()
elif sidebar == '🫁 Lung Cancer Predictor':
    show_lung_cancer_prediction_page()
elif sidebar == "📊 Explore":

    explore_option = st.sidebar.radio("Explore EDA for:", ["Diabetes", "Heart Attack", "Lung Cancer"])
    st.sidebar.markdown("""
    <style>
        .stRadio > label {
            color: black !important;
            font-weight: 600;
        }
        div[role="radiogroup"] > label {
            color: black !important;
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)
    if explore_option == "Diabetes":
        show_diabetes_explore_page()
    elif explore_option == "Heart Attack":
        show_heart_attack_explore_page()
    elif explore_option == "Lung Cancer":
        show_lung_cancer_explore_page()
elif sidebar == '🧾 Info':
    show_info()
elif sidebar == '👨‍💻 About Me':
    about_me()

# Footer
footer = """
<style>
footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px 0;
    width: 100vw;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
    z-index: 999999999;
    pointer-events: auto;
}
.footer-icons {
    text-align: center;
}
.footer-icons a {
    margin: 0 15px;
    text-decoration: none;
    display: inline-block;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.footer-icons a:hover {
    transform: scale(1.2);
    box-shadow: 0 0 12px #ffffff88;
}
.footer-icons img {
    width: 30px;
    height: 30px;
    vertical-align: middle;
}
</style>

<footer>
    <div class="footer-icons">
        <a href="https://github.com/Neev17964" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub">
        </a>
        <a href="https://www.instagram.com/its_neevs/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram">
        </a>
        <a href="https://www.linkedin.com/in/neevsharma" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
        </a>
    </div>
</footer>
"""

st.markdown(footer, unsafe_allow_html=True)
