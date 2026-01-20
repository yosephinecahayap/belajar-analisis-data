# E-Commerce Transaction Analysis Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk melakukan analisis data transaksi e-commerce secara end-to-end, mulai dari proses pengumpulan data, pembersihan data, analisis statistik deskriptif, hingga visualisasi dan analisis perilaku pelanggan menggunakan pendekatan **RFM (Recency, Frequency, Monetary)**.  
Hasil analisis disajikan dalam bentuk **dashboard interaktif menggunakan Streamlit** untuk mendukung pengambilan keputusan bisnis.

---

## Dataset yang Digunakan
Proyek ini menggunakan sembilan dataset e-commerce yang saling terhubung dan merepresentasikan keseluruhan proses bisnis.

- **Customers Dataset**  
  Menyimpan informasi identitas pelanggan dan lokasi geografis (kota dan state) yang digunakan untuk analisis distribusi pelanggan.

- **Geolocation Dataset**  
  Menyediakan informasi koordinat geografis berdasarkan kode pos untuk analisis persebaran pelanggan dan penjual.

- **Sellers Dataset**  
  Berisi informasi lokasi penjual yang digunakan untuk menganalisis distribusi penjual dan keterkaitannya dengan transaksi.

- **Products Dataset**  
  Memuat detail produk seperti kategori, deskripsi, dan dimensi produk untuk analisis performa kategori dan karakteristik produk.

- **Product Category Name Translation Dataset**  
  Digunakan sebagai tabel referensi untuk menerjemahkan kategori produk ke dalam bahasa Inggris agar hasil analisis lebih mudah dipahami.

- **Orders Dataset**  
  Dataset inti yang mencatat aktivitas pemesanan, status pesanan, dan waktu proses transaksi.

- **Order Reviews Dataset**  
  Menyimpan skor dan ulasan pelanggan yang digunakan untuk analisis tingkat kepuasan pelanggan.

- **Order Payments Dataset**  
  Berisi detail metode pembayaran dan nilai transaksi yang sangat penting untuk analisis pendapatan dan perhitungan nilai monetary.

- **Order Items Dataset**  
  Menyimpan detail item dalam setiap pesanan, termasuk harga produk dan biaya pengiriman.

---

## Tahapan Analisis Data

### Assessing Data
Evaluasi struktur, kelengkapan, dan kualitas data dilakukan pada seluruh dataset:
- Sebagian besar dataset tidak memiliki missing value.
- Missing value ditemukan pada dataset products, orders, dan order reviews.
- Missing value pada kolom tanggal pengiriman mencerminkan kondisi bisnis nyata (pesanan dibatalkan atau belum terkirim).

---

### Data Cleaning
Beberapa langkah pembersihan data yang dilakukan:
- Konversi kolom waktu ke tipe data `datetime`.
- Penggabungan beberapa dataset utama menjadi satu dataset terintegrasi dengan total **118.434 baris data**.
- Penghapusan baris data dengan missing value pada kolom transaksi penting seperti `product_id`, `price`, dan `payment_value`.
- Pengisian nilai kosong pada kategori produk dengan label **"Unknown"**.
- Missing value pada kolom tanggal pengiriman dibiarkan karena masih relevan secara bisnis.

---

### Analisis Statistik Deskriptif
Analisis statistik dilakukan untuk memahami karakteristik data transaksi:
- Transaksi berlangsung dari **September 2016 hingga Oktober 2018**, dengan puncak aktivitas pada akhir 2017–pertengahan 2018.
- Mayoritas pesanan hanya terdiri dari **1 item**.
- Distribusi harga dan nilai transaksi bersifat **right-skewed**, dipengaruhi oleh outlier bernilai tinggi.
- Biaya pengiriman merupakan komponen signifikan dalam transaksi.
- Pembayaran cicilan cukup umum digunakan oleh pelanggan.
- Produk umumnya berdimensi sedang dan berbobot relatif ringan.
- Ditemukan outlier pada harga, nilai transaksi, dan berat produk.

---

## Analisis & Insight Utama

### Pertanyaan 1  
**Kategori produk apa yang memberikan kontribusi pendapatan terbesar dan bagaimana persebarannya?**

**Insight:**
- Kategori **bed_bath_table** memberikan kontribusi pendapatan terbesar.
- Kategori **health_beauty** dan **computers_accessories** berada di posisi berikutnya.
- Beberapa kategori seperti *furniture_decor*, *watches_gifts*, dan *sports_leisure* memiliki kontribusi yang relatif stabil.
- Pendapatan tidak tersebar merata dan terkonsentrasi pada beberapa kategori unggulan.

**Conclusion:**
Kategori **bed_bath_table** merupakan penggerak utama pendapatan, diikuti oleh **health_beauty** dan **computers_accessories**. Hal ini menunjukkan bahwa produk kebutuhan rumah tangga, perawatan diri, dan aksesoris teknologi menjadi fokus utama bisnis. Strategi bisnis sebaiknya memprioritaskan penguatan kategori unggulan sambil tetap mengembangkan kategori lain yang berpotensi.

---

### Pertanyaan 2  
**Bagaimana pola perilaku pelanggan berdasarkan Recency, Frequency, dan Monetary (RFM)?**

**Insight:**
- Mayoritas pelanggan memiliki recency rendah, namun terdapat pelanggan tidak aktif dengan recency tinggi.
- Sebagian besar pelanggan hanya melakukan **1–2 transaksi**.
- Distribusi monetary didominasi nilai rendah.
- Sejumlah kecil pelanggan memiliki nilai monetary sangat tinggi dan berkontribusi besar terhadap total pendapatan.

**Conclusion:**
Analisis RFM menunjukkan bahwa bisnis sangat bergantung pada pelanggan bernilai tinggi meskipun jumlahnya sedikit. Selain itu, terdapat potensi churn pelanggan yang perlu diperhatikan. Oleh karena itu, strategi **retensi pelanggan loyal** dan **reaktivasi pelanggan tidak aktif** menjadi kunci dalam meningkatkan kinerja bisnis secara berkelanjutan.

---

## Tools yang Digunakan
- Python
- Pandas
- Matplotlib & Seaborn
- Streamlit
- Git & GitHub

---

## Cara Menjalankan Dashboard
### Setup Environment (Anaconda)
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Setup Environment (Shell / Terminal)
```bash
cd belajar-analisis-data-YosephineCahayaPermatahari
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### Menjalankan Aplikasi Streamlit
```bash
streamlit run dashboard.py
```
