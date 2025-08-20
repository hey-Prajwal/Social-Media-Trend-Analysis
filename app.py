import streamlit as st
import pandas as pd
from modules import eda, forecasting, sentiment, wordcloud_gen, recommend
from textblob import TextBlob

# --- Upload or Load Dataset ---
st.set_page_config(page_title="Social Media Trend Forecasting", layout="wide")
st.sidebar.title("📦 Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file, parse_dates=["Timestamp"])
    else:
        return pd.read_csv("simulated_social_media_data.csv", parse_dates=["Timestamp"])

df = load_data(uploaded_file)

# --- Sidebar Navigation ---
st.sidebar.title("📊 Social Media Trend Forecasting")
page = st.sidebar.radio("Select Module", [
    "Explore Data",
    "Forecast Trends",
    "Sentiment Analysis",
    "Word Cloud",
    "Recommendations"
])

# --- Page Router ---
if page == "Explore Data":
    eda.display_eda(df)

elif page == "Forecast Trends":
    hashtag = st.selectbox("Select a Hashtag to Forecast", df["Hashtag"].unique())
    forecasting.forecast_hashtag(df, hashtag)

elif page == "Sentiment Analysis":
    sentiment.analyze_sentiment(df)

elif page == "Word Cloud":
    wordcloud_gen.display_wordcloud(df, text_column="Text")

elif page == "Recommendations":
    # Ensure sentiment is available
    if "Sentiment" not in df.columns:
        df["Sentiment"] = df["Text"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        df["Sentiment_Label"] = df["Sentiment"].apply(
            lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral")
        )
    recommend.generate_recommendations(df)
    