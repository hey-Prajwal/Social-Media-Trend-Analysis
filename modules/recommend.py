import streamlit as st
import pandas as pd

def generate_recommendations(df):
    st.header("📈 Hashtag Recommendations")

    if 'Sentiment' not in df.columns or 'Hashtag' not in df.columns:
        st.warning("Sentiment or Hashtag data missing. Please run Sentiment Analysis first.")
        return

    # Group by hashtag and get average sentiment
    sentiment_avg = df.groupby('Hashtag')['Sentiment'].mean().reset_index()
    sentiment_avg.columns = ['Hashtag', 'Average Sentiment']

    # Group by hashtag and count appearances
    trend_count = df['Hashtag'].value_counts().reset_index()
    trend_count.columns = ['Hashtag', 'Frequency']

    # Merge both
    recommendation_df = pd.merge(sentiment_avg, trend_count, on='Hashtag')

    # Sort by sentiment and frequency
    top_recommendations = recommendation_df.sort_values(
        by=['Average Sentiment', 'Frequency'], ascending=False
    ).head(10)

    st.subheader("Top Recommended Hashtags")
    st.dataframe(top_recommendations)

    # Optionally plot
    st.bar_chart(top_recommendations.set_index('Hashtag')['Average Sentiment'])