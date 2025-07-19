import streamlit as st

def show_info():
    _, col, _ = st.columns(3)
    with col:
        st.header("🧾 INFORMATION")

    st.markdown("""
    ### 🧠 Models Used in Health Explorer
    Welcome to the brain of **Health Explorer** – where machine learning meets real-life health predictions!

    ---

    ## 💉 Diabetes & ❤️ Heart Attack Prediction:
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
                
    ### 🔍 Model Comparison for Diabetes Prediction

    We trained and evaluated several machine learning models to find the best-performing algorithm for diabetes prediction. Here's how each model performed:

    - **Logistic Regression** achieved an accuracy of **78.34%**
    - **Support Vector Classifier (SVC)** achieved an accuracy of **78.23%**
    - **K-Nearest Neighbors (KNN)** achieved an accuracy of **75.24%**
    - **Decision Tree** achieved an accuracy of **74.42%**
    - **Random Forest** achieved an accuracy of **77.84%**
    - **XGBoost Classifier** achieved an accuracy of **77.36%**

    After comparing the performance, **Logistic Regression** emerged as the most accurate model among all, with the hyperparameters **{'C': 0.1, 'penalty': 'l2'}**.  
    📌 **Hence, we selected Logistic Regression for making diabetes predictions in this application.**
                
    ---
                
    ### ❤️ Model Comparison for Heart Attack Prediction

    To ensure reliable heart attack risk assessment, we evaluated a range of machine learning models. The following are their respective accuracies:

    - **Logistic Regression** achieved an accuracy of **85.26%**
    - **Support Vector Classifier (SVC)** achieved an accuracy of **84.84%**
    - **K-Nearest Neighbors (KNN)** achieved an accuracy of **84.38%**
    - **Decision Tree** achieved an accuracy of **79.76%**
    - **Random Forest** achieved an accuracy of **83.57%**
    - **XGBoost Classifier** achieved an accuracy of **83.13%**

    After comparison, we found that **Logistic Regression** delivered the highest accuracy among all the models, with the hyperparameters **{'C': 10, 'penalty': 'l2'}**.  
    ✅ **Therefore, we used Logistic Regression for heart attack prediction in this app.**

    ---
                
    ## 🫁 Lung Cancer Prediction:
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
                
    ### 🫁 Model Comparison for Lung Cancer Prediction

    We trained and tested several classification models to detect lung cancer risk. Interestingly, most models achieved near-perfect accuracy, as shown below:

    - **Multinomial Logistic Regression** achieved an accuracy of **99.97%**
    - **K-Nearest Neighbors (KNN)** achieved an accuracy of **99.98%**
    - **Decision Tree** achieved an accuracy of **99.96%**
    - **Random Forest** achieved an accuracy of **99.97%**
    - **XGBoost Classifier** achieved an accuracy of **99.96%**

    Since **all models achieved almost 100% accuracy**, we chose to use **Multinomial Logistic Regression** due to its simplicity and interpretability.  
    🎯 **It’s efficient, fast, and perfect for our use case.**
                
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
