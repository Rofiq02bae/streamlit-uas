# eda_diabetes.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string

# Download stopwords (sekali saja)
nltk.download('stopwords')

# Load data dari GitHub
url = "https://raw.githubusercontent.com/dyt08/diabetes-prediction/refs/heads/main/dataset/Dataset%20of%20Diabetes.csv"
df = pd.read_csv(url)

# Cek dan tampilkan info dasar
print("📋 Info Dataset:")
print(df.info())
print("\n🔍 Cek missing values:")
print(df.isnull().sum())

# --- EDA & Visualisasi ---

# 1. Distribusi Fitur
plt.figure(figsize=(12, 6))
df.hist(bins=20, figsize=(14, 10), color='skyblue')
plt.suptitle('Distribusi Setiap Fitur')
plt.tight_layout()
plt.savefig('distribusi_fitur.png')
plt.close()

# 2. Korelasi Fitur Numerik
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriks Korelasi')
plt.tight_layout()
plt.savefig('korelasi_fitur.png')
plt.close()

# 3. Boxplot Berdasarkan CLASS
if 'CLASS' in df.columns:
    numeric_cols = numeric_df.columns.tolist()
    plt.figure(figsize=(16, 12))
    for i, col in enumerate(numeric_cols):
        plt.subplot(3, 4, i+1)
        sns.boxplot(data=df, x='CLASS', y=col)
        plt.title(f'{col} vs CLASS')
        plt.tight_layout()
    plt.suptitle('Distribusi Fitur berdasarkan Kelas', y=1.02)
    plt.savefig('boxplot_per_class.png')
    plt.close()

# 4. WordCloud (jika ada kolom teks)
if 'TEXT' in df.columns:
    all_text = " ".join(df['TEXT'].dropna().astype(str))
    stop_words = set(stopwords.words('english'))
    cleaned_text = " ".join([
        word.lower() for word in all_text.split()
        if word.lower() not in stop_words and word not in string.punctuation
    ])
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(cleaned_text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('WordCloud dari Teks')
    plt.tight_layout()
    plt.savefig('wordcloud.png')
    plt.close()
