import pandas as pd
import numpy as np
import os
import time
from faker import Faker


N_ROWS = 1_000_000 
CSV_FILE = 'data_mentah.csv'
PARQUET_FILE = 'data_terkompresi.parquet'

print(f"Membuat dataset dummy dengan {N_ROWS:,} baris...")
start_time = time.time()

fake = Faker()

data = {
    'ID_Transaksi': [f'TXN-{i:08d}' for i in range(N_ROWS)],
    'Nama_Pelanggan': [fake.name() for _ in range(N_ROWS)],
    'Region': np.random.choice(['Asia', 'Europe', 'America', 'Africa'], size=N_ROWS),
    'Kode_Produk': [f'PROD-{np.random.randint(1000, 9999)}' for _ in range(N_ROWS)],
    
    'Jumlah_Unit': np.random.randint(1, 100, size=N_ROWS, dtype=np.int32),
    'Harga_Per_Unit': np.round(np.random.uniform(10.00, 5000.00, size=N_ROWS), 2), 
    
    'Status_Lunas': np.random.choice([True, False], size=N_ROWS),
    'Tanggal_Transaksi': pd.to_datetime('2024-01-01') + pd.to_timedelta(np.random.randint(0, 365, size=N_ROWS), unit='D')
}

df = pd.DataFrame(data)

df['Total_Penjualan'] = df['Jumlah_Unit'] * df['Harga_Per_Unit']

df.to_csv(CSV_FILE, index=False)

end_time = time.time()
print(f"✅ Dataset CSV selesai dibuat dalam {end_time - start_time:.2f} detik.")
print("-" * 40)