# app.py
import streamlit as st
import pandas as pd
from PIL import Image
import os
import plotly.express as px

st.set_page_config(page_title="Dashboard Diabetes", layout="wide")

# Load data
url = "https://raw.githubusercontent.com/Bumbledebee/diabetes_dataset_analysis/refs/heads/main/diabetes_dataset.csv"
df = pd.read_csv(url)

# Title
st.title("🩺 Dashboard Interaktif Analisis Diabetes")
st.markdown("**Proyek ini menampilkan analisis eksploratif terhadap dataset pasien diabetes, dilengkapi dengan visualisasi dan insight interaktif.**")

# Tabs Navigasi
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📄 Dataset", 
    "📊 Statistik", 
    "📈 Visualisasi", 
    "☁️ WordCloud", 
    "🧠 Kesimpulan", 
    "📘 Penjelasan Fitur"
])

# Tab 1 - Data
with tab1:
    st.header("📄 Dataset dan Struktur")
    
    st.subheader("🧾 Data Sample")
    st.dataframe(df.head())

    st.subheader("🔍 Info Kolom")
    st.write(df.dtypes)

    st.subheader("❓ Missing Values")
    st.write(df.isnull().sum())

# Tab 2 - Statistik
with tab2:
    st.header("📊 Statistik Deskriptif")
    st.write(df.describe())

    if 'Outcome' in df.columns:
        st.subheader("📌 Distribusi Kelas (0 = Non-Diabetes, 1 = Diabetes)")
        class_counts = df['Outcome'].value_counts().sort_index()
        st.bar_chart(class_counts)
        st.markdown("""
    ✅ **Penjelasan:**
    - Nilai `0` berarti pasien **tidak mengidap diabetes (Non-Diabetes)**.
    - Nilai `1` berarti pasien **mengidap diabetes (Diabetes)**.
    - Grafik ini membantu kita memahami apakah jumlah pasien di setiap kelas **seimbang atau tidak**.
    - Jika data sangat tidak seimbang, maka **model prediksi bisa bias** dan perlu penyesuaian.
    """)

# Tab 3 - Visualisasi

with tab3:
    st.header("📈 Visualisasi EDA Interaktif")

    # Ambil kolom numerik
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    # Histogram interaktif
    fitur_hist = st.selectbox("Pilih fitur untuk histogram:", numeric_cols)
    fig_hist = px.histogram(df, x=fitur_hist, nbins=30, title=f"Histogram Distribusi {fitur_hist}")
    st.plotly_chart(fig_hist, use_container_width=True)

    # Heatmap korelasi interaktif
    corr = df.corr()
    fig_heatmap = px.imshow(corr, text_auto=True, aspect="auto", title="Heatmap Korelasi Fitur")
    st.plotly_chart(fig_heatmap, use_container_width=True)

    # Boxplot berdasarkan Outcome (label target)
    if 'Outcome' in df.columns:
        fitur_box = st.selectbox("Pilih fitur untuk boxplot berdasarkan Outcome:", numeric_cols)
        fig_box = px.box(df, x='Outcome', y=fitur_box, color='Outcome',
                         title=f"Boxplot {fitur_box} berdasarkan Outcome")
        st.plotly_chart(fig_box, use_container_width=True)

# Tab 4 - WordCloud
with tab4:
    st.header("☁️ WordCloud (Jika Ada Kolom TEXT)")
    if 'TEXT' in df.columns and os.path.exists("wordcloud.png"):
        st.image(Image.open("wordcloud.png"), caption="WordCloud dari Teks", use_column_width=True)
    else:
        st.warning("Tidak ada kolom teks 'TEXT' dalam dataset.")

# Tab 5 - Kesimpulan
with tab5:
    st.header("🧠 Ringkasan Insight dan Kesimpulan")
    st.markdown("Berikut adalah insight utama berdasarkan analisis dataset:")

    insight_data = {
        "Fitur": ["Glucose", "BMI", "Age", "Insulin", "BloodPressure"],
        "Insight": [
            "Glucose tinggi sangat berkaitan dengan kelas Diabetes.",
            "BMI tinggi lebih banyak muncul pada pasien Diabetes.",
            "Pasien yang lebih tua cenderung memiliki risiko lebih tinggi.",
            "Insulin rendah/tinggi memberi sinyal potensi Diabetes.",
            "BloodPressure lebih bervariasi, tetapi tetap berkontribusi."
        ]
    }

    insight_df = pd.DataFrame(insight_data)
    st.table(insight_df)

    st.markdown("""
    ### 📝 Kesimpulan Umum:
    - Fitur **Glucose**, **BMI**, dan **Insulin** memiliki pengaruh signifikan terhadap status Diabetes.
    - **Distribusi pasien tidak seimbang** (cek grafik distribusi kelas).
    - Data ini bisa digunakan lebih lanjut untuk **model prediksi** diabetes secara akurat.
    """)

    st.success("Proyek ini berhasil menyajikan analisis EDA dan dashboard interaktif yang informatif dan responsif.")

# Tab 6 - Penjelasan Fitur
with tab6:
    st.header("📘 Penjelasan Fitur pada Dataset")

    feature_desc = {
        "ID": "ID unik untuk tiap pasien (biasanya auto-generated).",
        "No_Pation": "Nomor rekam medis atau ID pasien dalam sistem rumah sakit.",
        "Gender": "Jenis kelamin pasien (Male atau Female).",
        "AGE": "Usia pasien dalam tahun.",
        "Pregnancies": "Jumlah kehamilan (hanya untuk pasien wanita).",
        "BMI": "Body Mass Index — ukuran kegemukan atau obesitas.",
        "Glucose": "Kadar glukosa dalam darah (indikator risiko diabetes).",
        "BloodPressure": "Tekanan darah pasien.",
        "HbA1c": "Persentase hemoglobin terglikasi, indikator kadar gula darah jangka panjang.",
        "LDL": "Low-Density Lipoprotein — kolesterol jahat.",
        "HDL": "High-Density Lipoprotein — kolesterol baik.",
        "Triglycerides": "Trigliserida dalam darah, jenis lemak yang berpengaruh pada risiko jantung.",
        "WaistCircumference": "Lingkar pinggang pasien (ukuran risiko metabolik).",
        "HipCircumference": "Lingkar pinggul pasien.",
        "WHR": "Waist to Hip Ratio — rasio lingkar pinggang terhadap pinggul.",
        "FamilyHistory": "Riwayat keluarga dengan diabetes (0 = tidak, 1 = ya).",
        "DietType": "Tipe pola makan pasien.",
        "Hypertension": "Status hipertensi (0 = tidak, 1 = ya).",
        "MedicationUse": "Penggunaan obat (0 = tidak, 1 = ya).",
        "Outcome": "Label target: 0 = Non-Diabetes, 1 = Diabetes."
    }

    desc_df = pd.DataFrame(
        list(feature_desc.items()),
        columns=["Fitur", "Deskripsi"]
    )

    st.table(desc_df)

    st.markdown("""
    📝 **Catatan:**
    - Fitur-fitur ini digunakan untuk evaluasi risiko diabetes.
    - Beberapa fitur juga membantu diagnosis penyakit terkait seperti hipertensi dan gangguan metabolik.
    """)
