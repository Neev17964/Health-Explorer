import streamlit as st

def show_home():
    st.set_page_config(page_title="Health Explorer", layout="wide")

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
        ("🩸", "Diabetes Prediction", "Assess your diabetes risk using multiple clinical indicators.", "diabetes"),
        ("❤️", "Heart Disease", "Evaluate your cardiovascular health with key medical metrics.", "heart"),
        ("🫁", "Lung Cancer", "Quick assessment of lung cancer risk based on your history.", "lung")
    ]

    for col, (icon, title, desc, page) in zip(cols, features_row1):
        with col:
            st.markdown(
                f"""
                <div style="position: relative;">
                    <div class="feature-card" onclick="window.location.href='/?page={page}'">
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

    cols = st.columns(3)
    features_row2 = [
        ("📊", "Explore", "Dive into visual insights from real-world datasets.", "dashboard"),
        ("🧾", "Information", "Transparency about datasets and models used.", "symptom-checker"),
        ("🤖", "CareBot", "Your friendly AI assistant for health Q&A. You can find it on the bottom right side.", "chatbot")
    ]

    for col, (icon, title, desc, page) in zip(cols, features_row2):
        with col: 
            st.markdown(
                f"""
                <div style="position: relative;">
                    <div class="feature-card" onclick="window.location.href='/?page={page}'">
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
