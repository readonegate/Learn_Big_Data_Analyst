# [ETS] Big Data Analysis – Machine Learning & KNIME

Repository ini berisi hasil pengerjaan proyek eksperimen untuk Evaluasi Tengah Semester mata kuliah Big Data Analysis Semester Ganjil 2025/2026.

## Identitas Mahasiswa

- Nama: Ridwan

- NIM: 20123030

- Kelas: A.23

## Pilihan Kasus

Case: A - Klasifikasi Tabular

Judul: Customer Churn Prediction

Deskripsi: Memprediksi apakah pelanggan akan berhenti berlangganan (Churn) atau tidak berdasarkan data historis penggunaan layanan.

## Sumber Data

Dataset yang digunakan dalam proyek ini adalah Telco Customer Churn.

Link Kaggle: https://www.kaggle.com/blastchar/telco-customer-churn

## Cara Menjalankan Notebook (Python)

1. Pastikan Anda memiliki Jupyter Notebook atau akses ke Google Colab.

2. Unduh file dataset Telco-Customer-Churn.csv dan file notebook .ipynb dari repository ini.

3. Buka file .ipynb.

```
Penting: Jika menggunakan Google Colab, upload file Telco-Customer-Churn.csv ke dalam session storage (panel kiri). Jika menggunakan Jupyter lokal, pastikan file CSV berada dalam satu folder dengan notebook.
```

Jalankan semua sel (Run All) untuk melihat proses preprocessing, training model, hingga evaluasi.

## Cara Membuka Workflow KNIME

1. Pastikan aplikasi KNIME Analytics Platform sudah terinstal di komputer Anda.

2. Unduh file workflow berekstensi .knwf dari repository ini.

3. Buka aplikasi KNIME.

4. Pilih menu File > Import KNIME Workflow...

5. Pilih file .knwf yang sudah diunduh, lalu klik Finish.

6. Klik tombol Execute All (tombol panah hijau ganda) untuk menjalankan seluruh workflow dari pembacaan data hingga scoring.

## Hasil Ringkas

Proyek ini membandingkan performa algoritma Logistic Regression dan Decision Tree untuk memprediksi churn pelanggan. Berdasarkan eksperimen menggunakan Python dan KNIME, model Logistic Regression menunjukkan performa yang sedikit lebih baik dan stabil dengan akurasi mencapai ~78.28% pada Python dan ~77.61% pada KNIME. Meskipun Decision Tree mampu mendeteksi jumlah pelanggan churn yang lebih banyak pada simulasi KNIME, Logistic Regression memberikan keseimbangan yang lebih baik antara presisi dan akurasi keseluruhan.