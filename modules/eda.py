import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def display_eda(df):
    st.header("📊 Exploratory Data Analysis")

    st.subheader("Preview Dataset")
    st.dataframe(df.head())

    st.subheader("Hashtag Frequency")
    hashtag_counts = df["Hashtag"].value_counts()
    st.bar_chart(hashtag_counts)

    st.subheader("Engagement Over Time")
    df_daily = df.groupby("Timestamp")[["Likes", "Shares", "Comments"]].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(data=df_daily, x="Timestamp", y="Likes", label="Likes", ax=ax)
    sns.lineplot(data=df_daily, x="Timestamp", y="Shares", label="Shares", ax=ax)
    sns.lineplot(data=df_daily, x="Timestamp", y="Comments", label="Comments", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)