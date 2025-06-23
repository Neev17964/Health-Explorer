import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache_data
def load_diabetes_data():
    return pd.read_csv("diabetes.csv")

def diabetes_heatmap():
    st.title("Diabetes Feature Correlation Heatmap")

    df = load_diabetes_data()

    corr_matrix = df.corr()
    st.subheader("Correlation Matrix Heatmap")
    st.write("""
        This heatmap shows the correlation between each feature and the diabetes outcome (1 = positive diagnosis).\n
        Higher correlation values indicate stronger relationships.
        """)
    col1, col2 = st.columns([3,1])
    with col1:

        fig, ax = plt.subplots(figsize=(10, 9))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
        st.pyplot(fig)
        
    st.markdown("""
        ### 🔍 Top 5 Insights
                    
#### 1) Glucose is the strongest predictor of diabetes
- ###### Correlation with Outcome: 0.47\n
- ###### this means that higher glucose levels are strongly associated with diabetes.
#### 2) BMI also shows a moderate correlation with diabetes
- ###### Correlation with Outcome: 0.29\n
- ###### People with higher BMI (body fat) are more likely to have diabetes.
#### 3) Age and diabetes have a positive relationship
- ###### Correlation with Outcome: 0.24\n
- ###### Which is normal because older individuals are slightly more prone to diabetes than younger ones, but the effect is less than glucose or BMI.
#### 4) Insulin and SkinThickness are correlated (0.44)
- ###### Though not directly tied strongly with Outcome, their inter-correlation indicates a physiological relationship (like metabolic indicators).
#### 5) Pregnancies and Age are highly correlated (0.54)
- ###### Makes sense naturally—more age, more chance of higher pregnancies—but also hints that age-related features should be treated carefully to avoid multicollinearity in modeling.
            """)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Top Features Related to Diabetes (by correlation with Outcome)")
    st.markdown(" If the value is closer to 1 then higher correlation if close to -1 then less correlation")
    target_corr = corr_matrix['Outcome'].drop('Outcome').sort_values(key=lambda x: abs(x), ascending=False)
    st.dataframe(target_corr)


def diabetes_sidebar():
    with st.sidebar:
        st.markdown("### Diabetes Feature's Info")
        st.markdown("""
        - **Pregnancies**: Number of times pregnant  
        - **Glucose**: Plasma glucose concentration  
        - **BloodPressure**: Diastolic blood pressure (mm Hg)  
        - **SkinThickness**: Triceps skin fold thickness (mm)  
        - **Insulin**: 2-Hour serum insulin (mu U/ml)  
        - **BMI**: Body mass index  
        - **DiabetesPedigreeFunction**: Diabetes pedigree function (hereditary risk)  
        - **Age**: Age in years  
        - **Outcome**: Class variable (0 = non-diabetic, 1 = diabetic)
        """)


def diabetes_histogram():

    df = load_diabetes_data()

    st.subheader("📊 Glucose Level Distribution Among Diabetic vs. Non-Diabetic Patients")
    st.markdown("0 --> Not Diabetic")
    st.markdown("1 --> Diabetic")

    plt.clf()
    col1, col2 = st.columns([2,1])
    with col1:
        fig, ax = plt.subplots(figsize = (5,3))
        sns.histplot(data=df, x="Glucose", hue="Outcome", kde=True, element="step", ax=ax)
        ax.set_title("Glucose Level Distribution by Diabetes Outcome")
        ax.set_xlabel("Glucose")
        ax.set_ylabel("Count")

        st.pyplot(fig)
    with col2:
        st.markdown("""## 🔍 Insights
- ##### We can easily observe that diabetic people tend to have more glucose level than non diabetic people.
- ##### This means if your glucose is above 120, it may indicate metabolic dysfunction.
- ##### And if it's above 150 then it strongly linked to diabetes complications.
""")


def diabetes_pairplot():

    df = load_diabetes_data()

    st.subheader("🔗 Pairplot of Selected Features")
    st.markdown("""
    This pairplot helps visualize the pairwise relationships between features in the dataset, 
    colored by diabetes outcome (0 = Non-Diabetic, 1 = Diabetic).
    """)

    selected_features = ['Glucose', 'BMI', 'Age', 'Insulin', 'Outcome']
    
    plt.clf()
    col1, col2 = st.columns([5,1])
    with col1:
        pair_plot = sns.pairplot(df[selected_features], hue="Outcome", palette="coolwarm", diag_kind="kde")

        st.pyplot(pair_plot.fig)
    
        st.markdown("""
### 📌 Insights from Pair Plot Analysis

#### 🔹 1. **Glucose Levels**
- Glucose stands out as a highly discriminative feature.
- Individuals with **Outcome = 1 (Diabetic)** show significantly higher glucose levels.
- The density plot clearly shows a separation between the two outcome groups.

#### 🔹 2. **BMI (Body Mass Index)**
- Higher BMI values are somewhat more associated with diabetic individuals.
- There is a visible shift in the density plot toward higher BMI ranges for Outcome = 1.
- However, the overlap between the two classes suggests BMI alone may not be sufficient for strong prediction.

#### 🔹 3. **Age**
- There is a mild trend of increasing diabetes risk with age.
- Diabetic individuals tend to fall in slightly older age brackets, though the separation is not strong.

#### 🔹 4. **Insulin Levels**
- The insulin feature shows high variance and overlap between the two outcomes.
- While there are some clusters of higher insulin in diabetics, the distribution is noisy and may require preprocessing or transformation for better utility.

#### 🔹 5. **Feature Interactions**
- **Glucose vs. Insulin**: Positively correlated — higher glucose often accompanies higher insulin.
- **BMI vs. Age**: Weak correlation, with some older individuals also showing higher BMI.
- **BMI vs. Insulin**: Shows some positive association, though still scattered.

---

### ✅ Summary
- **Glucose** is the most impactful feature.
- **BMI** and **Age** provide additional predictive value.
- **Insulin** might be useful after preprocessing due to its high variance and skewed distribution.
""")



def diabetes_bp_histplot():
    st.subheader("📊 Average Insulin Levels Across Glucose Ranges")
    df = load_diabetes_data()

    col1, col2 = st.columns([2,1])
    # Create glucose bins
    with col1:
        bins = [0, 80, 100, 120, 140, 160, 180, 200, 300]
        labels = ["0–80", "81–100", "101–120", "121–140", "141–160", "161–180", "181–200", "200+"]

        df["Glucose Range"] = pd.cut(df["Glucose"], bins=bins, labels=labels, include_lowest=True)

        # Group by glucose range and calculate mean insulin
        grouped = df.groupby("Glucose Range")["Insulin"].mean().reset_index()

        # Plot
        fig, ax = plt.subplots(figsize=(7, 4))
        sns.barplot(data=grouped, x="Glucose Range", y="Insulin", palette="mako", ax=ax)
        ax.set_title("Average Insulin Level by Glucose Range")
        ax.set_ylabel("Average Insulin Level")
        ax.set_xlabel("Glucose Range")

        st.pyplot(fig)

    with col2:
        st.markdown("""## 🔍 Insights
- ##### As **glucose level** increases, **average insulin level also increases**.
- ##### **Highest insulin level at 181-200 Glucose** which might suggest chances of diabetes.
- ##### After the **121-140** range, insulin secretion spikes  significantly which shows how the body intensifies insulin release as glucose exceeds **normal levels**.
- ##### The **0–80 glucose range** has the **lowest insulin** levels (~20 units).
""")



def diabetes_agegroup_lineplot():
    df = load_diabetes_data()

    bins = [20, 30, 40, 50, 60, 70, 100]
    labels = ["20-29", "30-39", "40-49", "50-59", "60-69", "70+"]
    df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)

    age_grouped = df.groupby("Age_Group")["Outcome"].mean().reset_index()
    age_grouped["Diabetes Rate (%)"] = age_grouped["Outcome"] * 100

    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("📈 Diabetes Rate by Age Group")
        fig, ax = plt.subplots(figsize = (5,3))
        sns.lineplot(data=age_grouped, x="Age_Group", y="Diabetes Rate (%)", marker="o", ax=ax)
        ax.set_title("Diabetes Rate by Age Group")
        ax.set_ylabel("Diabetes Rate (%)")
        ax.set_xlabel("Age Group")
        st.pyplot(fig)

    with col2:
        st.markdown("""## 🔍 Insights
- ##### We can easily observe that with increasing age the chances of having diabetes increases.
- ##### <40 years: Low risk (often linked to Type 1 diabetes or early metabolic issues).
- ##### 40–60 years: Rising risk (associated with lifestyle factors, prediabetes, and onset of Type 2 diabetes).
- ##### 50-59 years: Highest risk (due to aging, insulin resistance, and cumulative health effects).

""")