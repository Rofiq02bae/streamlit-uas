import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("📊 EDA Dashboard Interaktif")

# Upload
uploaded_file = st.file_uploader("Unggah file CSV kamu", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Pratinjau Data")
    st.dataframe(df.head())

    st.markdown("---")

    # Preprocessing sederhana
    st.subheader("🧼 Preprocessing")
    st.write("Jumlah nilai kosong per kolom:")
    st.dataframe(df.isnull().sum())

    if st.checkbox("Hapus baris dengan nilai kosong"):
        df.dropna(inplace=True)
        st.success("✔️ Nilai kosong dihapus")

    st.markdown("---")

    # Statistik deskriptif
    st.subheader("📈 Statistik Deskriptif")
    st.dataframe(df.describe())

    st.markdown("---")

    # Korelasi
    st.subheader("🔗 Korelasi antar variabel (numerik)")
    numeric_df = df.select_dtypes(include='number')
    if not numeric_df.empty:
        fig_corr, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig_corr)
    else:
        st.info("Data numerik tidak tersedia untuk korelasi.")

    st.markdown("---")

    # Visualisasi interaktif
    st.subheader("📊 Visualisasi Interaktif")
    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox("Pilih variabel X", df.columns)
    with col2:
        y_axis = st.selectbox("Pilih variabel Y", df.columns)

    chart_type = st.radio("Jenis Grafik", ["Scatter", "Line", "Histogram", "Box"])

    if chart_type == "Scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis)
    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_axis)
    elif chart_type == "Box":
        fig = px.box(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("⬆️ Silakan unggah file CSV untuk mulai.")
