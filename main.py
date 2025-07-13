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
    initial_sidebar_state="collapsed"
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

# --- SIDEBAR LOGIC FIX ---
# Use session state to handle sidebar selection for navigation buttons
if 'sidebar_selection' not in st.session_state:
    st.session_state.sidebar_selection = "🏠 Home"

sidebar = st.sidebar.selectbox(
    "Choose a section",
    options=[
        "🏠 Home",
        "💉 Diabetes Predictor",
        "❤️ Heart Attack Predictor",
        "🫁 Lung Cancer Predictor",
        "📊 Explore",
        "🧾 Info",
        "👨‍💻 About Me"
    ],
    index=[
        "🏠 Home",
        "💉 Diabetes Predictor",
        "❤️ Heart Attack Predictor",
        "🫁 Lung Cancer Predictor",
        "📊 Explore",
        "🧾 Info",
        "👨‍💻 About Me"
    ].index(st.session_state.sidebar_selection),
    label_visibility="collapsed"
)

st.session_state.sidebar_selection = sidebar

# Main page routing
if sidebar == '🏠 Home':
    # 🎨 Custom CSS with animation + styling
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(180deg, #3a7bd5, #00d2ff) !important;
        }
        button[kind="secondary"] {
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            height: 0 !important;
        }
        .header-content {
            background: white;
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            border-left: 5px solid #0288d1;
            text-align: center;
            margin-bottom: 2rem;
        }
        .animated-title {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(270deg, #0288d1, #0277bd, #01579b, #0288d1);
            background-size: 800% 800%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: flowGradient 4s linear infinite;
            margin: 0;
        }
        .animated-subtitle {
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 10px;
            position: relative;
            left: -15px;
            background: linear-gradient(270deg, #b3e5fc, #0288d1, #01579b, #b3e5fc);
            background-size: 800% 800%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: flowGradient 4s linear infinite;
        }
        .animated-box {
            background: linear-gradient(135deg, #8ec5fc, #e0c3fc);
            padding: 0.1rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(74, 20, 140, 0.5);
            text-align: center;
            transition: all 0.4s ease-in-out;
        }
        .animated-text {
            font-size: 2rem;
            font-weight: 600;
            color: black;
            position: relative;
            left: -30px;
        }
        .pulse-emoji {
            animation: pulse 1.5s infinite;
            display: inline-block;
        }
        .animated-subbox {
            background: linear-gradient(135deg, #a18cd1, #fbc2eb);
            padding: 0.1rem;
            border-radius: 16px;
            margin-top: 10px;
            box-shadow: 0 4px 20px rgba(162, 93, 220, 0.4);
            text-align: center;
            transition: all 0.4s ease-in-out;
        }
        .animated-subbox p {
            font-size: 1.9rem;
            font-weight: 600;
            color: black;
            margin: 0;
        }
        .bounce-arrow {
            display: inline-block;
            animation: bounceDown 1.4s infinite;
            font-size: 2rem;
        }
        @keyframes bounceDown {
            0%   { transform: translateY(0); }
            50%  { transform: translateY(8px); }
            100% { transform: translateY(0); }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        @keyframes flowGradient {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }
        .feature-container {
            margin-bottom: 30px;
        }
        .feature-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            padding-bottom: 150px;
            height: 150px;
            margin: 10px 0;
            border-left: 5px solid #0288d1;
            box-shadow: 0 4px 12px rgba(2, 136, 209, 0.2);
            color: #0d47a1;
            transition: all 0.3s ease;
            position: relative;
            z-index: 1;
        }
        button.stButton > button {
            background-color: #111 !important;
            color: #fff !important;
            border: 2px solid #222 !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: background 0.2s, color 0.2s;
        }
        button.stButton > button:hover {
            background-color: #111 !important;
            color: #90caf9 !important;
            border-color: #0288d1 !important;
        }
        .feature-card:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 24px rgba(1, 87, 155, 0.3);
        }
        .feature-icon {
            font-size: 2.5rem;
            margin: 0;
            color: #0277bd;
        }
        .feature-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: black;
            margin: 0;
        }
        .footer-credit {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            font-size: 1rem;
            margin-top: 0rem;
        }
        .footer-credit strong {
            color: #e3f2fd;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 🧠 Header
    _, colb, _ = st.columns([1,3,1])
    with colb:
        st.markdown(
            """
            <div class="header-content">
                <h1 class="animated-title">Welcome to Health Explorer 🩺</h1>
                <p class="animated-subtitle" style="font-size:1.2rem">Your AI-powered health companion for disease prediction & insights</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 📢 Instruction Box w/ emoji
    _,col,_ = st.columns([1,2.5,1])
    with col:
        st.markdown(
            """
            <div class="animated-box">
                <p style="font-size:2rem; font-weight:600; color:black; margin:0;">
                    Ready to explore your health? <span class="pulse-emoji">😊</span>
                </p>
                <p class="animated-text" style="font-size:1.8rem">🡐 Use the sidebar to navigate</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    _,col1,_ = st.columns([1,2,1])
    with col1:
        st.markdown(
            """
            <div class="animated-subbox">
                <p style="font-size:2rem; font-weight:600; color:black; margin:0;">
                    These are the features this website offers <span class="bounce-arrow">🢃</span>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 💠 Feature Cards
    st.markdown('<div class="feature-container">', unsafe_allow_html=True)

    cols = st.columns(3)
    features_row1 = [
        ("🩸", "Diabetes Predictor", "Assess your diabetes risk using multiple clinical indicators.", "💉 Diabetes Predictor"),
        ("❤️", "Heart Disease Predictor", "Evaluate your cardiovascular health with key medical metrics.", "❤️ Heart Attack Predictor"),
        ("🫁", "Lung Cancer Predictor", "Quick assessment of lung cancer risk based on your history.", "🫁 Lung Cancer Predictor")
    ]

    for col, (icon, title, desc, page) in zip(cols, features_row1):
        with col:
            st.markdown(
                f"""
                <div style="position: relative;">
                    <div class="feature-card">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                            <div class="feature-icon">{icon}</div>
                            <div class="feature-title">{title}</div>
                        </div>
                        <p>{desc}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"{icon} Go to {title}", key=f"btn_{page}"):
                st.session_state.sidebar_selection = page
                st.rerun()

    cols = st.columns(3)
    features_row2 = [
        ("📊", "Explore", "Dive into visual insights from real-world datasets.", "📊 Explore"),
        ("🧾", "Information", "Transparency about datasets and models used.", "🧾 Info"),
        ("🤖", "CareBot", "Your friendly AI assistant for health Q&A. You can find it on the bottom right side.", "chatbot")
    ]

    for col, (icon, title, desc, page) in zip(cols, features_row2):
        with col: 
            st.markdown(
                f"""
                <div style="position: relative;">
                    <div class="feature-card">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                            <div class="feature-icon">{icon}</div>
                            <div class="feature-title">{title}</div>
                        </div>
                        <p>{desc}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if page != "chatbot":
                if st.button(f"{icon} Go to {title}", key=f"btn_{page}"):
                    st.session_state.sidebar_selection = page
                    st.rerun()
            else:
                if st.button(f"{icon} {title}", key=f"btn_{page}"):
                    st.markdown("""
                                <div style="
                                    background-color: #007bff;
                                    border: 2px solid #0056b3;
                                    padding: 1rem;
                                    border-radius: 10px;
                                    color: white;
                                    font-weight: 500;
                                    margin-top: 1rem;
                                ">
                                    💬 CareBot is already active! Look for the chat interface on the bottom right side of your screen.
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔚 Enhanced Footer with Darker Container
    st.markdown("---")
    st.markdown(
        """
        <style>
        .footer-container {
            background: linear-gradient(135deg, #0277bd 0%, #01579b 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin-top: 2rem;
            box-shadow: 0 4px 12px rgba(1, 87, 155, 0.3);
        }
        .footer-credit {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            font-size: 1rem;
            color: white;
        }
        .footer-credit strong {
            color: #e3f2fd;
            font-weight: 600;
        }
        .footer-icon {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { opacity: 0.8; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.1); }
            100% { opacity: 0.8; transform: scale(1); }
        }
        </style>
        
        <div class="footer-container">
            <div class="footer-credit">
                <span class="footer-icon">✔</span>
                <span>Built with Python by <strong>Neev</strong> | Medical AI Assistant</span>
                <span class="footer-icon">💙</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main routing for other pages
if sidebar == '💉 Diabetes Predictor':
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
