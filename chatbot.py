import streamlit as st
import streamlit.components.v1 as components
from streamlit_float import float_init, float_box
from PIL import Image
import base64
import os

def Chatbot():
    # Initialize floating behavior
    float_init()

    # Session toggle
    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False

    # Load image and encode to base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Ensure image exists
    img_path = "CareBot.png"
    if not os.path.exists(img_path):
        st.warning("CareBot.png not found!")
        return

    img_base64 = get_base64_of_bin_file(img_path)

    # Create button using form
    with st.form(key="chat_form", clear_on_submit=False):
        submit = st.form_submit_button(
            label="",
            use_container_width=True
        )

        # Custom CSS for square image button
        st.markdown(f"""
            <style>
                [data-testid="stForm"] {{
                    position: fixed;
                    bottom: 30px;
                    right: 20px;
                    width: 50px;
                    height: 80px;
                    padding: 0;
                    margin: 0;
                    overflow-x: hidden !important;
                    background-color: transparent;
                }}
                [data-testid="stForm"] button {{
                    width: 100%;
                    height: 100%;
                    border: none;
                    background-image: url("data:image/png;base64,{img_base64}");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-position: center;
                    cursor: pointer;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                    transition: transform 0.2s ease-in-out;
                }}
                [data-testid="stForm"] button:hover {{
                    transform: scale(1.1);
                }}
            </style>
        """, unsafe_allow_html=True)

    # Toggle chatbot visibility
    if submit:
        st.session_state.chat_open = not st.session_state.chat_open

    # Show chatbot iframe if open
    if st.session_state.chat_open:
        iframe_html = """
        <iframe src="https://www.chatbase.co/chatbot-iframe/Qc6Q8XGc33jY6P-kmBBd1"
        style="width:100%; height:100%; border:none;"></iframe>
        """
        float_box(
            iframe_html,
            width="350px", height="575px",
            right="0px", bottom="120px",
            css="box-shadow: 0 4px 16px rgba(0,0,0,0.25); border-radius:8px;",
            shadow=12,
            z_index="999999"
        )
