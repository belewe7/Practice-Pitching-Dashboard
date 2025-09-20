# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 01:19:40 2025

@author: belew
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel("pitching_metrics.xlsx")

# Calculate Perceived Velocity
df["Perceived_Velocity"] = df["Velocity"] * (60.5 / (60.5 - df["Extension"]))

st.title("Pitching Dashboard (Practice)")

# Select pitchers to display
pitchers = df["Pitcher"].unique()
selected_pitchers = st.sidebar.multiselect("Choose pitchers", pitchers, default=pitchers)

# Filter data
filtered_df = df[df["Pitcher"].isin(selected_pitchers)]

# Show data table
st.write("### Pitching Data with Perceived Velocity")
st.dataframe(filtered_df)

# Plot average Perceived Velocity by pitch type
if "PitchType" in df.columns:
    avg_pv = filtered_df.groupby("PitchType")["Perceived_Velocity"].mean()
    fig, ax = plt.subplots()
    avg_pv.plot(kind="bar", ax=ax, color="skyblue")
    ax.set_ylabel("MPH")
    ax.set_title("Average Perceived Velocity by Pitch Type")
    st.pyplot(fig)
