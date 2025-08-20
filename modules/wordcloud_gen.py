import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def display_wordcloud(data, text_column='text'):
    st.header("Word Cloud")

    if data is None or text_column not in data.columns:
        st.warning("No data or invalid column selected.")
        return

    text = " ".join(data[text_column].astype(str).tolist())

    if not text.strip():
        st.warning("No valid text to generate word cloud.")
        return

    wordcloud = WordCloud(
        width=800, height=400, background_color='white', max_words=200
    ).generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)