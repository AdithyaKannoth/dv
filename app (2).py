import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Load dataset
df = sns.load_dataset("tips")


# App TitLe
st.title("Interactive Data Visualization with Streamlit")


# Sidebar for dataset exploration
st.sidebar.header("Data Exploration")


# Show raw dataset
if st.sidebar.checkbox("show Raw Data"):
    st.subheader("Dataset Preview")
    st.write(df.head())


# seLect visualization Type
chart_type = st.sidebar.selectbox(
"select Chart Type", ["Scatter Plot","Box Plot", "Histogram"]
)


# Scatter PLot
if chart_type == "scatter Plot":
    st.subheader("Scatter Plot: Total Bill vs Tip")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df["total_bill"], y=df["tip"], hue=df["sex"], ax=ax)
    st.pyplot(fig)


#Box PLot
elif chart_type == "Box Plot":
    st.subheader("Box Plot: Tip Amount by Day")
    fig, ax = plt.subplots()
    sns.boxplot(x="day", y="tip", data=df,palette="set2",ax=ax)
    st.pyplot(fig)




# Histogram (Updated Fix)
elif chart_type == "Histogram":
    st.subheader("Histogram of Total Bill")
    fig, ax =plt.subplots()
    sns.histplot(np.array(df["total_bill"]), bins=28, kde=True, ax=ax)
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Frequency")
    st.pyplot(fig)

if st.sidebar.checkbox("show Correlation Heatmap"):
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)