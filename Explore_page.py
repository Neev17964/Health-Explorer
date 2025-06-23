import streamlit as st
from Diabetes_EDA import diabetes_heatmap, diabetes_sidebar, diabetes_histogram, diabetes_pairplot, diabetes_agegroup_lineplot, diabetes_bp_histplot

from Heart_Attack_EDA import heart_attack_heatmap, heart_attack_sidebar, heart_attack_histogram, heart_attack_pairplot,age_distribution_histogram, heart_attack_chest_pain_countplot

from Lung_Cancer_EDA import cancer_heatmap, cancer_sidebar, cancer_airpollution_countplot, cancer_agegroup_countplot, cancer_gender_risk_stacked_bar, cancer_genetic_risk_subplot

def show_diabetes_explore_page():
    diabetes_heatmap()

    diabetes_sidebar()
    
    st.markdown("<hr>", unsafe_allow_html=True)

    diabetes_histogram()

    st.markdown("<hr>", unsafe_allow_html=True)

    diabetes_pairplot()

    st.markdown("<hr>", unsafe_allow_html=True)

    diabetes_bp_histplot()

    st.markdown("<hr>", unsafe_allow_html=True)

    diabetes_agegroup_lineplot()

    
def show_heart_attack_explore_page():
    heart_attack_heatmap()

    heart_attack_sidebar()

    st.markdown("<hr>", unsafe_allow_html=True)

    heart_attack_histogram()

    st.markdown("<hr>", unsafe_allow_html=True)

    heart_attack_pairplot()

    st.markdown("<hr>", unsafe_allow_html=True)

    age_distribution_histogram()

    st.markdown("<hr>", unsafe_allow_html=True)

    heart_attack_chest_pain_countplot()

def show_lung_cancer_explore_page():
    cancer_heatmap()

    cancer_sidebar()

    st.markdown("<hr>", unsafe_allow_html=True)

    cancer_airpollution_countplot()

    st.markdown("<hr>", unsafe_allow_html=True)

    cancer_agegroup_countplot()

    st.markdown("<hr>", unsafe_allow_html=True)

    cancer_gender_risk_stacked_bar()

    st.markdown("<hr>", unsafe_allow_html=True)

    cancer_genetic_risk_subplot()