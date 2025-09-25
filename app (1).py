import streamlit as st
import pandas as pd
import datetime
import os

# Nama file CSV
FILE_NAME = 'data_suhu.csv'

# Fungsi untuk mencatat suhu
def catat_suhu(suhu):
    tanggal = datetime.date.today()
    new_data = pd.DataFrame([[tanggal, suhu]], columns=['Tanggal', 'Suhu'])
    if os.path.exists(FILE_NAME):
        new_data.to_csv(FILE_NAME, mode='a', index=False, header=False)
    else:
        new_data.to_csv(FILE_NAME, index=False)
    st.success("✅ Suhu berhasil dicatat!")

# Fungsi untuk membaca data suhu
def baca_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME, parse_dates=['Tanggal'])
    else:
        return pd.DataFrame(columns=['Tanggal', 'Suhu'])

st.title("🌡️ Aplikasi Pemantau Suhu Harian")

menu = st.sidebar.radio("Menu", ["Catat Suhu Hari Ini", "Lihat Data Suhu"])

if menu == "Catat Suhu Hari Ini":
    st.subheader("Catat Suhu Hari Ini")
    suhu = st.number_input("Masukkan suhu hari ini (°C)", min_value=-50.0, max_value=60.0, step=0.1)
    if st.button("Simpan"):
        catat_suhu(suhu)

elif menu == "Lihat Data Suhu":
    st.subheader("📊 Data Suhu Harian")
    df = baca_data()
    if df.empty:
        st.warning("Belum ada data suhu!")
    else:
        st.dataframe(df)
        # Tambah grafik sederhana
        df['Tanggal'] = pd.to_datetime(df['Tanggal'])
        df = df.sort_values('Tanggal')
        st.line_chart(df.set_index('Tanggal')['Suhu'])
