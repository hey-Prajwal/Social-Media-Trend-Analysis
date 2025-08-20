# sentiment.py
import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_sentiment(df):
    st.title("💬 Sentiment Analysis")

    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity

    df["Sentiment"] = df["Text"].apply(get_sentiment)
    df["Sentiment_Label"] = df["Sentiment"].apply(
        lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral")
    )

    sentiment_counts = df["Sentiment_Label"].value_counts()

    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots()
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis", ax=ax)
    ax.set_ylabel("Number of Posts")
    st.pyplot(fig)

    st.write("Sample Sentiment Data:")
    st.dataframe(df[["Text", "Sentiment", "Sentiment_Label"]].head())

    return df
