import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache_data
def load_heart_attack_data():
    return pd.read_csv("heart.csv")

def heart_attack_heatmap():
    st.title("Heart Attack Feature Correlation Heatmap")
    st.write("""
    This heatmap shows the correlation between each feature and the probability of a heart attack (target = 1).\n
    Higher correlation values indicate stronger relationships.
    """)

    df = load_heart_attack_data()

    corr_matrix = df.corr()

    st.subheader("Correlation Matrix Heatmap")

    col1, col2 = st.columns([4,1])
    with col1:
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
        st.pyplot(fig)
    st.markdown("""
### 🔍 Top 5 Insights from Heart Attack Correlation Analysis

#### 1) **Chest Pain (cp) is the strongest predictor of heart attack**
- ###### Correlation with Target: 0.43\n
- ###### Patients with chest pain are significantly more likely to have a heart attack.

#### 2) **Maximum Heart Rate (thalach) shows strong positive correlation**
- ###### Correlation with Target: 0.42\n
- ###### Higher maximum heart rate during exercise indicates higher heart attack risk.

#### 3) **Exercise-Induced Angina (exang) is a critical risk factor**
- ###### Correlation with Target: -0.44\n
- ###### Negative correlation means absence of angina lowers heart attack risk.

#### 4) **ST Depression (oldpeak) strongly predicts heart attack**
- ###### Correlation with Target: -0.43\n
- ###### Higher ST depression indicates greater heart stress and risk.

#### 5) **Number of Major Vessels (ca) is a key indicator**
- ###### Correlation with Target: -0.39\n
- ###### Fewer open vessels (higher blockage) increases heart attack risk.

#### **Bonus Insight**
- ###### Age has weaker but notable correlation (0.23)\n
- ###### While age contributes, other factors are stronger direct predictors.
""")
    with col2:
        pass

    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Top Features Related to Heart Attack (by correlation with target)")
    st.markdown(" If the value is closer to 1 then higher correlation if close to -1 then less correlation")
    target_corr = corr_matrix['target'].drop('target').sort_values(key=lambda x: abs(x), ascending=False)
    st.dataframe(target_corr)


def heart_attack_sidebar():
    with st.sidebar:
        st.markdown("### Heart Attack Feature's Info")
        st.markdown("""
        - **age**: Age of the patient  
        - **sex**: Gender (1 = Male, 0 = Female)  
        - **cp**: Chest pain type (0–3)  
        - **trestbps**: Resting blood pressure  
        - **chol**: Serum cholesterol  
        - **fbs**: Fasting blood sugar > 120 mg/dl  
        - **restecg**: Resting ECG results  
        - **thalach**: Max heart rate  
        - **exang**: Exercise-induced angina  
        - **oldpeak**: ST depression  
        - **slope**: Slope of ST segment  
        - **ca**: Major vessels colored by fluoroscopy  
        - **thal**: Thalassemia type  
        - **target**: Heart disease (1 = yes, 0 = no)
        """)


def heart_attack_histogram():

    df = load_heart_attack_data()

    st.subheader("📊 Cholesterol Level Distribution Among Heart Attack Outcomes")
    st.markdown("""
    This histogram shows how cholesterol levels vary among patients who had a heart attack (`target = 1`) and those who did not (`target = 0`).
    """)

    col1, col2 = st.columns([2,1])
    with col1:
        plt.clf()
        sns.histplot(data=df, x="chol", hue="target", kde=True, element="step", palette="Set1")
        plt.title("Cholesterol Level Distribution by Heart Attack Outcome")
        plt.xlabel("Cholesterol")
        plt.ylabel("Count")
        st.pyplot(plt.gcf())
    
    with col2:
        st.markdown("""
## 🔍 Insights
- ##### Individuals with heart attacks tend to have higher cholesterol levels compared to those without.
- ##### Healthy individuals typically maintain cholesterol below 200 mg/dL.
- ##### Cholesterol levels between 200-300 mg/dL indicate increased cardiovascular risk.
- ##### Levels above 300 mg/dL are strongly associated with heart attack occurrence.
""")


def heart_attack_pairplot():

    df = load_heart_attack_data()

    st.subheader("🔗 Pairplot of Selected Heart Features")
    st.markdown("""
    This pairplot helps visualize the pairwise relationships between features in the dataset, 
    colored by heart attack outcome (`target`).
    """)

    selected_features = ['age', 'chol', 'thalach', 'oldpeak', 'target']

    col1, col2 = st.columns([5,1])

    with col1:
        plt.clf()
        pair_plot = sns.pairplot(df[selected_features], hue="target", palette="coolwarm", diag_kind="kde")
        st.pyplot(pair_plot.fig)

        st.markdown("""
### 📌 Insights from Pair Plot Analysis

#### 🔹 1. **Age**
- Slightly higher age appears to be associated with heart disease (target = 1), though the overlap is substantial.
- The density plot suggests that middle-aged individuals (40–60) are more likely to be in the heart disease group.

#### 🔹 2. **Cholesterol (chol)**
- Cholesterol levels do not show a clear distinction between the two target classes.
- High variance and overlap indicate that cholesterol alone may not be a strong predictive factor in this dataset.

#### 🔹 3. **Maximum Heart Rate Achieved (thalach)**
- Thalach is one of the more discriminative features.
- Individuals with **lower maximum heart rates** tend to have heart disease.
- The density plots show a clear shift: those with **higher thalach** are mostly non-diseased (target = 0).

#### 🔹 4. **Oldpeak**
- Oldpeak (ST depression induced by exercise relative to rest) shows good separation.
- Individuals with **higher oldpeak values** are more likely to have heart disease.
- This makes it a strong indicator for target = 1.

#### 🔹 5. **Feature Interactions**
- **thalach vs. age**: Inversely related — older individuals tend to have lower maximum heart rate.
- **oldpeak vs. thalach**: Slight inverse trend — higher ST depression often coincides with lower heart rate.
- Other pairings like **chol vs. age** show no significant correlation.

---

### ✅ Summary
- **thalach** and **oldpeak** show the most promise as predictive features.
- **Age** adds moderate value.
- **Cholesterol** does not appear to contribute significantly to class separation in this visualization.
""")


def age_distribution_histogram():

    df = load_heart_attack_data()

    st.subheader("📊 Age Distribution vs Heart Attack")
    st.markdown("""
    This histogram shows how age is distributed among patients with and without heart attacks. 
    The KDE curve helps visualize the density of age across both groups.
    """)

    col1, col2 = st.columns([2,1])

    with col1:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(data=df, x="age", hue="target", kde=True, element="step", palette="husl", bins=20, ax=ax)
        ax.set_title("Age Distribution with Heart Attack Status")
        ax.set_xlabel("Age")
        ax.set_ylabel("Frequency")
        ax.legend(title="Heart Attack", labels=["No", "Yes"])
        st.pyplot(fig)

    with col2:
        st.markdown("""
## 🔍 Insights
- ##### Heart attack cases are significantly more common in individuals aged 50+ years.
- ##### Younger individuals (below 40) rarely experience heart attacks.
- ##### The highest heart attack frequency occurs between ages 50-70.
- ##### Age 60 appears to be the peak risk period for heart attacks.
""")


def heart_attack_chest_pain_countplot():
    df = load_heart_attack_data()

    st.subheader("📈 Chest Pain Type Distribution by Heart Attack Outcome")
    st.markdown("""
    This count plot shows how different types of chest pain are distributed among people who did and did not experience a heart attack.
    """)

    col1, col2 = st.columns([2,1])

    with col1:
        plt.clf()
        fig, ax = plt.subplots()

        cp_mapping = {
            0: "Typical Angina",
            1: "Atypical Angina", 
            2: "Non-anginal Pain",
            3: "Asymptomatic"
        }

        df['cp_label'] = df['cp'].map(cp_mapping)

        sns.countplot(data=df, x="cp_label", hue="target", palette="Set1", ax=ax,
                    order=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
        ax.set_xlabel("Chest Pain Type")
        ax.set_ylabel("Count")
        ax.set_title("Chest Pain Type vs Heart Attack Outcome")
        ax.legend(title="Heart Attack", labels=["No (0)", "Yes (1)"])

        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

        df.drop('cp_label', axis=1, inplace=True)
    
    with col2:
        st.markdown("""
## 🔍 Insights
- ##### Non-anginal Pain patients show the highest rate of heart attacks.
- ##### Typical Angina cases have the lowest heart attack occurrence.
""")