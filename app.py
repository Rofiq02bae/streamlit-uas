# app.py
import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(page_title="Dashboard Diabetes", layout="wide")

# Load data
url = "https://raw.githubusercontent.com/dyt08/diabetes-prediction/refs/heads/main/dataset/Dataset%20of%20Diabetes.csv"
df = pd.read_csv(url)

# Title
st.title("🩺 Dashboard Interaktif Analisis Diabetes")

# Tabs Navigasi
tab1, tab2, tab3, tab4 = st.tabs(["📄 Dataset", "📊 Statistik", "📈 Visualisasi", "☁️ WordCloud"])

# Tab 1 - Data
with tab1:
    st.subheader("🧾 Data Sample")
    st.dataframe(df.head())

    st.subheader("🔍 Info Kolom")
    st.write(df.dtypes)

    st.subheader("❓ Missing Values")
    st.write(df.isnull().sum())

# Tab 2 - Statistik
with tab2:
    st.subheader("📈 Statistik Deskriptif")
    st.write(df.describe())

    if 'CLASS' in df.columns:
        st.subheader("📊 Distribusi Kelas")
        st.bar_chart(df['CLASS'].value_counts())

# Tab 3 - Visualisasi
with tab3:
    st.subheader("🔹 Histogram Distribusi")
    if os.path.exists("distribusi_fitur.png"):
        st.image(Image.open("distribusi_fitur.png"), use_column_width=True)

    st.subheader("🔹 Korelasi Antar Fitur")
    if os.path.exists("korelasi_fitur.png"):
        st.image(Image.open("korelasi_fitur.png"), use_column_width=True)

    st.subheader("🔹 Boxplot Berdasarkan CLASS")
    if os.path.exists("boxplot_per_class.png"):
        st.image(Image.open("boxplot_per_class.png"), use_column_width=True)

# Tab 4 - WordCloud
with tab4:
    if 'TEXT' in df.columns and os.path.exists("wordcloud.png"):
        st.subheader("☁️ WordCloud dari Kolom TEXT")
        st.image(Image.open("wordcloud.png"), use_column_width=True)
    else:
        st.warning("Tidak ada kolom teks 'TEXT' pada dataset.")
