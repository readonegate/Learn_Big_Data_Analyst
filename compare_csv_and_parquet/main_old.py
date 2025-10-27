import pandas as pd
import os
import time

CSV_FILE = 'compare_csv_and_parquet/data_mentah.csv'
PARQUET_FILE = 'compare_csv_and_parquet/data_terkompresi.parquet'


print(f"Membaca {CSV_FILE} ke Pandas DataFrame...")
start_time = time.time()

read_df = pd.read_csv(CSV_FILE, dtype={
    'ID_Transaksi': 'string',
    'Nama_Pelanggan': 'string',
    'Region': 'category',
    'Kode_Produk': 'string',
    'Jumlah_Unit': 'int32',
    'Harga_Per_Unit': 'float64',
    'Status_Lunas': 'boolean',
    'Total_Penjualan': 'float64'
})

end_time = time.time()
print(f"✅ DataFrame selesai dimuat dalam {end_time - start_time:.2f} detik.")

print(f"Menyimpan kembali DataFrame ke {PARQUET_FILE} (Kolumnar, Terkompresi)...")
start_time = time.time()


read_df.to_parquet(PARQUET_FILE, index=False, engine='pyarrow', compression='snappy')

end_time = time.time()
print(f"✅ File Parquet selesai disimpan dalam {end_time - start_time:.2f} detik.")
print("-" * 40)


print("Menghitung perbandingan ukuran file:")

csv_size_bytes = os.path.getsize(CSV_FILE)
parquet_size_bytes = os.path.getsize(PARQUET_FILE)

csv_size_mb = csv_size_bytes / (1024 * 1024)
parquet_size_mb = parquet_size_bytes / (1024 * 1024)

# Hitung rasio
ratio = csv_size_mb / parquet_size_mb

print(f"  Ukuran file CSV ({CSV_FILE}):        {csv_size_mb:.2f} MB ({csv_size_bytes:,} bytes)")
print(f"  Ukuran file Parquet ({PARQUET_FILE}): {parquet_size_mb:.2f} MB ({parquet_size_bytes:,} bytes)")
print("-" * 40)
print(f"**HASIL AKHIR: File Parquet JAUH lebih kecil ({ratio:.2f}x lebih kecil dari CSV)!**")
print("\nDemo Konseptual Selesai.")