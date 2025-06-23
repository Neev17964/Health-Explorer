import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache_data
def load_cancer_data():
    return pd.read_csv("cancer.csv")

def cancer_heatmap():
    st.title("Cancer Feature Correlation Heatmap")

    df = load_cancer_data()

    df['LevelEncoded'] = df['Level'].map({'Low': 0, 'Medium': 1, 'High': 2})
    corr_matrix = df.drop(['Patient Id', 'Level'], axis=1).corr()

    st.subheader("Correlation Matrix Heatmap")
    st.write("""
    This heatmap shows how features correlate with one another. Values closer to 1 or -1 indicate stronger relationships.
    """)

    col1, col2 = st.columns([4,1])

    with col1:
        fig, ax = plt.subplots(figsize=(14, 10))
        sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', linewidths=0.5, ax=ax)
        st.pyplot(fig)

    st.markdown("""
### 🔍 Top 5 Insights

#### 1) **Smoking is the strongest predictor of lung cancer risk**
- ###### Correlation with Risk Level: **0.70**
- ###### A high positive correlation indicates that smoking is a major risk factor for lung cancer.

#### 2) **Genetic Risk also plays a significant role**
- ###### Correlation with Risk Level: **0.66**
- ###### Individuals with a family history of lung cancer are much more likely to develop it.

#### 3) **Air Pollution is a strong environmental contributor**
- ###### Correlation with Risk Level: **0.63**
- ###### Prolonged exposure to polluted air increases lung cancer risk.

#### 4) **Chronic Lung Disease is a major clinical indicator**
- ###### Correlation with Risk Level: **0.62**
- ###### Pre-existing lung conditions significantly raise the chances of developing lung cancer.

#### 5) **Passive Smoking contributes notably to risk**
- ###### Correlation with Risk Level: **0.59**
- ###### Even non-smokers exposed to second-hand smoke face elevated risk.

#### **Bonus Insight**
- ###### **Balanced Diet** shows a negative correlation (**-0.56**) with lung cancer risk.
- ###### Indicates that maintaining a healthy diet may have protective effects.
""")



    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Top Features Correlated with Cancer Level")
    st.markdown(" If the value is closer to 1 then higher correlation if close to -1 then less correlation")
    target_corr = corr_matrix['LevelEncoded'].drop('LevelEncoded').sort_values(key=lambda x: abs(x), ascending=False)
    st.dataframe(target_corr)

def cancer_sidebar():
    with st.sidebar:
        st.markdown("### Cancer Feature's Info")
        st.markdown("""
        - **Age**: Age of the patient  
        - **Gender**: 1 = Male, 2 = Female  
        - **Air Pollution**: Exposure level (1-10)  
        - **Alcohol use**: Frequency/intensity (1-10)  
        - **Dust Allergy**: Severity level (1-10)  
        - **Occupational Hazards**: Exposure at workplace (1-10)  
        - **Genetic Risk**: Family history (1-10)  
        - **Chronic Lung Disease**: Severity (1-10)  
        - **Balanced Diet**: Quality (1-10)  
        - **Obesity**: Obesity level (1-10)  
        - **Smoking**: Smoking frequency (1-10)  
        - **Passive Smoker**: Exposure to passive smoke (1-10)  
        - **Chest Pain**: Intensity (1-10)  
        - **Coughing of Blood**: Frequency (1-10)  
        - **Fatigue**: Level of fatigue (1-10)  
        - **Weight Loss**: Degree of weight loss (1-10)  
        - **Shortness of Breath**: Severity (1-10)  
        - **Wheezing**: Occurrence (1-10)  
        - **Swallowing Difficulty**: Difficulty level (1-10)  
        - **Clubbing of Finger Nails**: Presence (1-10)  
        - **Frequent Cold**: Frequency (1-10)  
        - **Dry Cough**: Intensity (1-10)  
        - **Snoring**: Frequency (1-10)  
        - **Level**: Risk level (Low, Medium, High)
        """)


def cancer_airpollution_countplot():
    df = load_cancer_data()

    st.subheader("🧪 Cancer Risk vs. Air Pollution Exposure")
    st.markdown("""
    This count plot shows how cancer risk levels (Low, Medium, High) vary across different air pollution exposure scores.
    """)

    col1 , col2 = st.columns([3,2])

    with col1:
        plt.clf()
        fig, ax = plt.subplots(figsize=(10, 7))
        sns.countplot(data=df, x="Air Pollution", hue="Level", palette="coolwarm", ax=ax)

        ax.set_title("Cancer Risk Levels by Air Pollution Exposure")
        ax.set_xlabel("Air Pollution Score")
        ax.set_ylabel("Count")

        st.pyplot(fig)

    with col2:
        st.markdown("""
## 🔍 Insights
- ##### High air pollution exposure shows the strongest association with cancer risk.
- ##### Medium exposure levels demonstrate moderate cancer risk correlation.
- ##### Low pollution areas have the lowest observed cancer incidence rates.
- ##### The risk gradient is clearly visible: High > Medium > Low pollution.
- ##### Cancer cases increase proportionally with pollution exposure levels.
""")


def cancer_agegroup_countplot():
    df = load_cancer_data()

    st.subheader("📈 Cancer Risk Cases by Age Group")
    st.markdown("""
    This count plot shows the distribution of cancer risk levels across age groups.
    """)

    col1, col2 = st.columns([2,1])

    with col1:
        bins = [10, 20, 30, 40, 50, 60, 70]
        labels = ['10-19', '20-29', '30-39', '40-49', '50-59', '60+']
        df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

        plt.clf()
        fig, ax = plt.subplots(figsize=(10, 7))
        sns.countplot(data=df, x="AgeGroup", hue="Level", palette="pastel", ax=ax)
        ax.set_title("Cancer Risk Level by Age Group")
        ax.set_xlabel("Age Group")
        ax.set_ylabel("Count")

        st.pyplot(fig)

    with col2:
        st.markdown("""
## 🔍 Insights
- ##### Cancer risk increases significantly with age, showing lowest rates in 10-19 age group.
- ##### The **30-39** age group shows the highest proportion of High Risk cases.
- ##### Medium Risk cases become noticeable starting from 30-39 age group.
- ##### Low Risk predominates in younger populations (10-29 years).
""")

def cancer_gender_risk_stacked_bar():
    df = load_cancer_data()

    st.subheader("🧍‍♂️🧍‍♀️ Cancer Risk Distribution by Gender")
    st.markdown("""
    This stacked bar chart shows how cancer risk levels (Low, Medium, High) are distributed between male and female patients.
    """)

    df["Gender"] = df["Gender"].map({1: "Male", 2: "Female"})
    gender_risk_counts = df.groupby(["Gender", "Level"]).size().unstack().fillna(0)

    col1, col2 = st.columns([2,1])

    with col1:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        gender_risk_counts.plot(kind='bar', stacked=True, ax=ax, colormap="Set2")

        ax.set_title("Cancer Risk Level by Gender")
        ax.set_xlabel("Gender")
        ax.set_ylabel("Number of Patients")
        ax.legend(title="Risk Level")
        st.pyplot(fig)

    with col2:
        st.markdown("""
## 🔍 Insights
- ##### Males show higher prevalence of High Risk cases compared to females.
- ##### Females demonstrate greater proportion of Low Risk cases.
- ##### Medium Risk distribution appears relatively similar across genders.
- ##### Gender differences are most pronounced in High Risk category.
""")

def cancer_genetic_risk_subplot():
    df = load_cancer_data()

    df["Level"] = pd.Categorical(df["Level"], categories=["Low", "Medium", "High"], ordered=True)

    st.subheader("🧬 Genetic Risk vs Cancer Risk Level")

    col1, col2 = st.columns([4,3])

    with col1:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(data=df, x="Genetic Risk", hue="Level", palette="coolwarm", ax=ax)
        ax.set_title("Cancer Risk Level Distribution by Genetic Risk Score")
        ax.set_xlabel("Genetic Risk (1 = Low Risk Genes, 7 = High Risk Genes)")
        ax.set_ylabel("Number of Patients")
        st.pyplot(fig)
    
    with col2:
        st.markdown("""
## 🔍 Insights

- ##### There is a clear trend showing that **higher genetic risk scores are associated with a higher cancer risk level**.
- ##### **Patients with low genetic risk (1–3)** are mostly in the **Low or Medium** cancer risk levels.
- ##### **Genetic Risk Score = 7** shows the highest count in the **High risk category**, marking it a strong indicator.
- ##### This shows that **genetic predisposition significantly impacts cancer risk** and should aid early detection.
""")