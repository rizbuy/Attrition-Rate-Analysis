# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis

Tingkat Attrition pada perusahaan Jaya Jaya Maju yang mencapai lebih dari 10% berdampak negatif pada perusahaan. Dikarenakan perusahaan dengan tingkat attrition yang tinggi harus merekrut dan melatih karyawan baru yang mempengaruhi kondisi finansial perusahaan. Perusahaan ingin mengetahui apa saja faktor yang mempengaruhi tingginya tingkat attrition pada perusahaan Jaya Jaya Maju.

### Cakupan Proyek

Proyek ini bertujuan untuk menganalisis berbagai faktor penyebab tingginya attrition karyawan. Ruang lingkup pekerjaan meliputi pengembangan business dashboard sebagai alat pemantauan dan pengelolaan faktor tersebut, serta pembangunan model machine learning untuk memprediksi risiko pengunduran diri karyawan di masa depan.

### Persiapan

Sumber data: employee_data.csv

Setup environment:


1. Clone this Repository
   ```bash
   git clone https://github.com/aNdr3W03/Employee-Attrition-Problem.git
   ```

2. Create Python Virtual Environment
   ```bash
   uv venv --python 3.12
   ```

2. Activate the Environment
   ```bash
   venv\Scripts\activate
   ```

4. Install All the Requirements Inside "requirements.txt"
   ```bash
   uv pip install -r requirements.txt
   ```


## Business Dashboard

[Jaya Jaya Maju Employees Dashboard](https://lookerstudio.google.com/reporting/c861ad31-9b42-4c5f-a854-fd19a9c3b03b), dashboard ini memberikan insight kepada para stakeholder terkait tingkat attrition yang cukup tinggi hingga lebih dari 10%. visualisasi berbagai faktor pada dashboard ini memudahkan para stakeholder untuk meninjau variabel yang berpengaruh pada tingginya tingkat attrition pada perusahaan Jaya Jaya Maju

![Jaya Jaya Maju Attrition Analysis] (Looker Studio Dashboard.jpg)

Analisis Dashboard Attrition
Dashboard ini menyajikan visualisasi data untuk memantau indikator utama dan faktor-faktor yang mempengaruhi attrition (pengunduran diri) karyawan. Secara garis besar, data menunjukkan jumlah karyawan aktif sebanyak 879 orang dengan total attrition 179 orang, sehingga menghasilkan Attrition Rate sebesar 16.92%.

1. Demografi dan Pendidikan
Attrition by Education: Karyawan dengan latar belakang pendidikan Bachelor (Sarjana) merupakan penyumbang angka attrition tertinggi (mendekati 80 orang), diikuti oleh lulusan Master. Lulusan tingkat Doctor memiliki angka attrition yang paling rendah. Attrition by Marital Status: Berdasarkan status pernikahan, mayoritas karyawan yang keluar berstatus Single (Lajang) yaitu sebesar 52.5%, diikuti oleh karyawan yang sudah Married (34.6%) dan Divorced (12.8%).

2. Departemen dan Perjalanan Bisnis
Department by Attrition: Departemen Research & Development menyumbang angka attrition terbesar yaitu 59.8%, disusul oleh departemen Sales sebesar 36.9%, dan Human Resources yang paling kecil. Attrition by Business Travel: Frekuensi perjalanan dinas sangat berpengaruh. Karyawan yang Rarely Travel (jarang bepergian) memiliki jumlah attrition tertinggi (di atas 100 orang), jauh lebih tinggi dibandingkan mereka yang sering bepergian (Travel Frequently) atau tidak bepergian sama sekali.

3. Tren Masa Kerja dan Indikator Keuangan
Attrition by Years at Company: Grafik garis menunjukkan bahwa risiko attrition sangat tinggi pada masa awal kerja, khususnya di tahun pertama hingga tahun kedua. Angka ini menurun drastis seiring bertambahnya masa kerja, menunjukkan bahwa karyawan yang sudah melewati masa 10 tahun cenderung lebih stabil.

Indikator Rata-rata:

* Rata-rata Usia: 37.06 tahun.

* Rata-rata Pendapatan Bulanan: 6,625.95.

* Rata-rata Jarak dari Rumah: 8.98 unit.

## Conclusion

Beriku adalah beberapa poin kesimpulan yang dapat diambil dari dashboard:

- Profil Risiko Tinggi (Early Attrition): Tingkat attrition paling kritis terjadi pada 2 tahun pertama masa kerja karyawan. Hal ini mengindikasikan adanya masalah pada proses adaptasi atau ekspektasi peran di awal karier.

- Dominasi Status Lajang: Lebih dari separuh karyawan yang keluar (52.5%) berstatus Single. Kelompok ini cenderung memiliki mobilitas tinggi dan lebih sensitif terhadap penawaran eksternal dibandingkan karyawan yang sudah berkeluarga.

- Masalah di Departemen Teknis: Departemen Research & Development (59.8%) dan Sales (36.9%) merupakan penyumbang utama kehilangan talenta. Tingginya angka di R&D perlu diwaspadai karena menyangkut aset intelektual perusahaan.

- Korelasi Pendidikan: Karyawan dengan tingkat pendidikan Bachelor (Sarjana) menunjukkan volume pengunduran diri terbesar, yang mungkin disebabkan oleh banyaknya peluang pasar bagi lulusan strata satu.

### Rekomendasi Action Items (Optional)

Untuk menurunkan tingkat attrition sebesar 16.92%, berikut adalah langkah konkret yang disarankan:

- Program Retensi untuk Karyawan Baru (0-5 Tahun):

Menerapkan sistem mentorship yang lebih intensif bagi karyawan di bawah masa kerja 5 tahun untuk membantu adaptasi budaya dan peran.

Melakukan evaluasi berkala (kuesioner atau stay interview) pada bulan ke-6 dan ke-12 untuk mendeteksi dini ketidakpuasan.

- Optimalisasi di Departemen R&D & Sales:

Melakukan survei spesifik di departemen R&D untuk mengidentifikasi apakah attrition disebabkan oleh beban kerja yang repetitif atau kurangnya fasilitas riset yang memadai.

- Review Struktur Kompensasi & Benefit:

Mengingat rata-rata pendapatan berada di angka 6,625.95, perusahaan perlu melakukan benchmarking gaji dengan kompetitor di industri yang sama untuk memastikan bahwa kompensasi tetap kompetitif bagi karyawan berprestasi tinggi.

- Peninjauan Kebijakan Business Travel:

Mengevaluasi kembali apakah karyawan yang "Jarangi bepergian" (Rarely Travel) merasa kurang dilibatkan dalam proyek strategis atau merasa stagnan di posisi mereka.

- Penguatan Engagement untuk Karyawan Single:

Membangun program keterlibatan karyawan (employee engagement) yang lebih dinamis agar karyawan lajang merasa lebih terikat secara emosional dengan komunitas kantor.


