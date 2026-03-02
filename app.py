import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Airline Insights Dashboard - Milestone 2")

df = pd.read_csv("airline.csv")
df['Departure Date'] = pd.to_datetime(df['Departure Date'])
df['Month'] = df['Departure Date'].dt.month
df['DayOfWeek'] = df['Departure Date'].dt.day_name()

menu = st.sidebar.selectbox("Select Analysis",
                            ["Univariate",
                             "Bivariate",
                             "Delay Analysis"])

if menu == "Univariate":
    fig, ax = plt.subplots()
    sns.countplot(x='Gender', data=df, ax=ax)
    st.pyplot(fig)

elif menu == "Bivariate":
    fig, ax = plt.subplots()
    sns.countplot(x='Flight Status', hue='Gender', data=df, ax=ax)
    st.pyplot(fig)

elif menu == "Delay Analysis":
    df['IsDelayed'] = df['Flight Status'].apply(lambda x: 1 if x == "Delayed" else 0)
    monthly_delay = df.groupby('Month')['IsDelayed'].mean()

    fig, ax = plt.subplots()
    monthly_delay.plot(marker='o', ax=ax)
    st.pyplot(fig)