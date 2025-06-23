import streamlit as st

def show_info():
    _, col, _ = st.columns(3)
    with col:
        st.header("🧾 INFORMATION")

    st.markdown("""
    ### 🧠 Models Used in Health Explorer
    Welcome to the brain of **Health Explorer** – where machine learning meets real-life health predictions!

    ---

    #### 💉 Diabetes & ❤️ Heart Attack Prediction:
    We use a **Logistic Regression Model** – a simple yet powerful algorithm used for binary classification problems. In our case:
    - **0 = No Disease**
    - **1 = Disease Present**

    **How it works:**
    - The logistic regression model uses a mathematical function called the **sigmoid function** to squash the output between 0 and 1 (which we interpret as probability).
    - If the predicted probability > 0.5 → classified as **1 (positive)**, else **0 (negative)**.

    **Sigmoid Function Graph:**""", unsafe_allow_html=True)

    st.image("Sigmoid Graph.png", width=250)

    st.markdown("""
    **Sigmoid Function:**""", unsafe_allow_html= True)

    st.image("Sigmoid Function Formula.png", width = 150)

    st.markdown("""
    This gives the probability of a person having a disease based on input health metrics (like glucose, age, blood pressure etc).

    ---

    #### 🫁 Lung Cancer Prediction:
    This one’s more complex – we use a **Multinomial Logistic Regression Model** because:
    - We have **three classes**:
    - 0 → High Risk
    - 1 → Low Risk
    - 2 → Moderate Risk

    **How it works:**
    - Instead of just sigmoid, we use the **softmax function**, which turns raw scores into probabilities for multiple classes.
    - The model assigns probabilities for each of the 3 risk categories, and the highest one is the prediction.

    **Softmax Function:**""", unsafe_allow_html=True)
    st.image("Softmax Function Formula.png", width=150)
    st.markdown("""
    Each input feature like **smoking, pollution, obesity, fatigue, snoring** etc. contributes to the final prediction.

    ---

    ### 📊 Model Highlights:
    - All models were **custom implemented from scratch** using only **NumPy** 💪
    - Trained using **gradient descent**, optimizing weights to reduce prediction error
    - Scaled inputs using **Standard Scaler** for faster and more stable training

    ---

    ### 💻 Entire Project Stack:
    - **Frontend:** Streamlit (for interactive UI)
    - **Backend Models:** Logistic Regression & Multinomial Logistic Regression
    - **ML Libraries:** NumPy, pandas, scikit-learn
    - **Visualization:** Seaborn & Matplotlib

    Hope you enjoyed the tech peek 👨‍💻. If you're curious how the chatbot works too – it was made in **chatbase** by me and was trained on relevant data of diabetes, lung cancer and heart attack. 🚀
    """, unsafe_allow_html=True)


    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style='text-align: center;'>
            <p><span style = "font-size: 20px;"</span> The dataset I used for Diabetes Prediction</p>
            <p><span style="font-size: 32px;"</span>👇</p>
            <p style="font-size: 32px;">
                <a href="https://drive.google.com/file/d/1yJDR_NJKXu7KGjUF641dAEaCoMm2YHHK/view?usp=sharing" target="_blank">📁</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
    """
    <div style='text-align: center;'>
        <p><span style = "font-size: 20px;"</span> The dataset I used for Heart Attack Prediction</p>
        <p><span style="font-size: 32px;"</span>👇</p>
        <p style="font-size: 32px;">
            <a href="https://drive.google.com/file/d/14Nh1hjsq2y7X7MnsyCVVzRJUN-005Rfh/view" target="_blank">📁</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
    
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
    """
    <div style='text-align: center;'>
        <p><span style = "font-size: 20px;"</span> The dataset I used for Lung Cancer Prediction</p>
        <p><span style="font-size: 32px;"</span>👇</p>
        <p style="font-size: 32px;">
            <a href="https://drive.google.com/file/d/1vgCViiqYE9gFnc_zJNX0Jkb3mEsnQip1/view?usp=sharing" target="_blank">📁</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)