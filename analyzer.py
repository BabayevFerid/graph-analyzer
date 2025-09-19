import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def load_data(file_path):
    """CSV faylını oxuyur və DataFrame qaytarır."""
    try:
        df = pd.read_csv(file_path)
        print("\n✅ Fayl uğurla oxundu!\n")
        return df
    except Exception as e:
        print(f"❌ Xəta: {e}")
        sys.exit(1)

def show_summary(df):
    """Məlumatların statistik xülasəsini göstərir."""
    print("\n📊 Məlumatların xülasəsi:\n")
    print(df.describe(include="all"))

def plot_column(df, x_col, y_col):
    """İki sütun arasında qrafik çəkir."""
    try:
        plt.figure(figsize=(10,5))
        plt.plot(df[x_col], df[y_col], marker="o", linestyle="-", color="blue")
        plt.title(f"{y_col} vs {x_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"❌ Qrafik çəkilmədi: {e}")

def main():
    print("📈 Qrafik Analizator\n")

    # Data faylı
    file_path = "data/sample.csv"
    if not os.path.exists(file_path):
        print(f"❌ Fayl tapılmadı: {file_path}")
        sys.exit(1)

    # Məlumatları yüklə
    df = load_data(file_path)

    # Sütunları göstər
    print("\n📑 Fayldakı sütunlar:")
    for col in df.columns:
        print(f"- {col}")

    # Statistik məlumat
    show_summary(df)

    # İstifadəçidən sütun seçmək
    x_col = input("\nX oxu üçün sütun seçin: ")
    y_col = input("Y oxu üçün sütun seçin: ")

    if x_col not in df.columns or y_col not in df.columns:
        print("❌ Yanlış sütun adı daxil edildi!")
        sys.exit(1)

    # Qrafik çək
    plot_column(df, x_col, y_col)

if __name__ == "__main__":
    main()
