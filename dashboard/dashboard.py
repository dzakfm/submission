import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Analisis Data Rental Sepeda')

#mengambil dataset
bike_day_df = pd.read_csv("all_data.csv")

st.subheader("Dataset Preview")
st.dataframe(bike_day_df.head())

#data berdasarkan season
season_rental = bike_day_df.groupby(by="season").agg({
    "cnt": "nunique"
}).reset_index()

#tampilan dataset rental per season
st.subheader("Rental per Season")
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(season_rental['season'], season_rental['cnt'], 
        marker='o', color='b', linestyle='-', linewidth=2, markersize=8)
ax.set_xlabel('Season')
ax.set_ylabel('Jumlah Rental')
ax.set_title('Total Rental per Season')
ax.grid(True)
st.pyplot(fig)

#data berdasarkan weekday
weekday_rental = bike_day_df.melt(id_vars=["weekday"], value_vars=["casual", "registered"],
                                   var_name="Tipe Pengguna", value_name="Jumlah Pengguna")

#tampilan dataset rental per weekday
st.subheader("Pengguna Casual dan Registered per Weekday")
plt.figure(figsize=(10, 6))
sns.barplot(x="weekday", y="Jumlah Pengguna", hue="Tipe Pengguna", data=weekday_rental, palette="Set2")
plt.title("Pengguna Casual dan Registered per Weekday", fontsize=16)
plt.xlabel("Weekday", fontsize=12)
plt.ylabel("Jumlah Pengguna", fontsize=12)
st.pyplot(plt.gcf())

#download dataset csv
st.subheader("Download Dataset")
csv = bike_day_df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="all_data.csv",
    mime="text/csv"
)