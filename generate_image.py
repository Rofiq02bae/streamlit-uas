import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi buat gambar visualisasi
def generate_images(df):
    os.makedirs('images', exist_ok=True)

    plt.figure(figsize=(14, 10))
    df.hist(bins=20, figsize=(14,10), color='skyblue')
    plt.suptitle('Distribusi Setiap Fitur')
    plt.tight_layout()
    plt.savefig('images/distribusi_fitur.png')
    plt.close()

    plt.figure(figsize=(12,10))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Matriks Korelasi Fitur')
    plt.tight_layout()
    plt.savefig('images/korelasi_fitur.png')
    plt.close()

    if 'Outcome' in df.columns:
        numeric_cols = df.select_dtypes(include='number').columns.drop('Outcome')
        plt.figure(figsize=(20, 15))
        for i, col in enumerate(numeric_cols):
            plt.subplot(4, 5, i+1)
            sns.boxplot(data=df, x='Outcome', y=col)
            plt.title(f'{col} berdasarkan Outcome')
        plt.tight_layout()
        plt.savefig('images/boxplot_per_class.png')
        plt.close()

# Panggil generate gambar saat app start
generate_images(df)

# ... lalu di bagian Streamlit kamu load gambar dari 'images/' seperti biasa
