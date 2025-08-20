# forecasting.py
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import streamlit as st


def forecast_hashtag(df, hashtag):
    tag_df = df[df["Hashtag"] == hashtag]
    tag_counts = tag_df.groupby("Timestamp").size().reset_index(name="Count")
    tag_counts.columns = ["ds", "y"]  # Prophet expects 'ds' and 'y'

    if len(tag_counts) < 2:
        st.warning("Not enough data to forecast this hashtag.")
        return None

    model = Prophet()
    model.fit(tag_counts)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    # Plotting
    fig1 = model.plot(forecast)
    st.pyplot(fig1)

    return forecast