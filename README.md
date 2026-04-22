# 🎬 Actor Collaboration Network Analysis

**Indonesian Action Film Industry using Knowledge Graph & Graph Data Science**

---

## 📌 Overview

Project ini berfokus pada analisis jejaring kolaborasi aktor dalam industri film aksi Indonesia dengan memanfaatkan pendekatan Knowledge Graph. Penelitian ini bertujuan untuk memahami bagaimana aktor-aktor saling terhubung melalui film yang mereka bintangi, serta mengidentifikasi pola kolaborasi yang terbentuk dalam jaringan tersebut.

Untuk memperoleh data yang lebih komprehensif, dilakukan integrasi data dari Wikidata dan DBpedia Indonesia. Data yang telah diintegrasikan kemudian direpresentasikan dalam bentuk graph untuk dianalisis menggunakan Graph Data Science.

---

## 🎯 Objectives

* Menganalisis pola kolaborasi antar aktor dalam film aksi Indonesia
* Mengidentifikasi aktor yang memiliki peran penting dalam jaringan
* Mengelompokkan aktor berdasarkan hubungan kolaborasi
* Mengungkap struktur tersembunyi dalam jaringan aktor–film

---

## 📊 Study Case

Dataset berfokus pada:

* 🎭 Actor
* 🎬 Film (Action - Indonesia)
* 🔗 Relasi: `Act_in`

### 🔗 Sumber Data

* Wikidata (SPARQL endpoint)
* DBpedia Indonesia

---

## ⚙️ Data Integration Process

Proses integrasi data dilakukan secara sederhana namun efektif dengan menggabungkan data dari dua sumber utama menggunakan pendekatan berbasis preprocessing dan concatenation.

### 1. Data Extraction

Data diambil dari Wikidata dan DBpedia dalam format CSV:

```bash
wikidata_data.csv  
dbpedia_data.csv
```

---

### 2. Data Selection & Normalization

Dari Wikidata, hanya atribut yang relevan yang digunakan, yaitu:

* `filmLabel` → film
* `actorLabel` → actor

Sementara dari DBpedia, dilakukan normalisasi string untuk mengubah format URI menjadi nama yang lebih mudah dibaca:

* Mengambil bagian terakhir dari URL
* Mengganti underscore (`_`) menjadi spasi

Contoh:

```bash
http://dbpedia.org/resource/The_Raid → The Raid
```

---

### 3. Data Merging (Concatenation)

Data dari kedua sumber tidak dilakukan join berbasis key, melainkan digabungkan menggunakan metode concatenation untuk mengumpulkan seluruh relasi aktor–film dari kedua dataset.

Pendekatan ini dipilih karena:

* Tidak semua entitas memiliki key yang konsisten antar sumber
* Tujuan utama adalah memperkaya relasi, bukan menyamakan entitas secara eksplisit

---

### 4. Data Cleaning

Dilakukan pembersihan data untuk meningkatkan kualitas dataset:

* Menghapus suffix seperti `(film)`
* Menghilangkan whitespace berlebih
* Normalisasi teks agar konsisten

---

### 5. Deduplication

Setelah data digabung, dilakukan penghapusan duplikasi berdasarkan pasangan:

* `(film, actor)`

Hal ini memastikan tidak ada relasi yang redundan dalam graph.

---

📁 Output akhir:

```bash
combined_data_final.csv
```

---

## 🔍 Graph Algorithms

### 1. 🔗 Similarity (Node Similarity - Jaccard)

Analisis kemiripan dilakukan menggunakan algoritma Node Similarity dengan pendekatan Jaccard Similarity.

Digunakan untuk mengukur kemiripan antar aktor berdasarkan film yang mereka bintangi.

**Insight:**

* Aktor dengan pola kolaborasi serupa
* Potensi rekomendasi aktor untuk proyek film

---

### 2. ⭐ Centrality (PageRank)

Analisis centrality menggunakan algoritma PageRank untuk mengidentifikasi aktor yang memiliki pengaruh tinggi dalam jaringan.

**Insight:**

* Aktor paling sentral dalam industri
* Aktor yang menjadi penghubung antar jaringan

---

### 3. 🧩 Community Detection (Louvain)

Deteksi komunitas menggunakan algoritma Louvain Method dengan optimasi Modularity.

**Insight:**

* Kelompok aktor yang sering bekerja sama
* Struktur komunitas dalam film aksi Indonesia

---

## 🛠️ Tech Stack

* Python (Pandas) → Data integration
* SPARQL → Data extraction
* Neo4j + Graph Data Science → Graph analysis

---

## 📈 Output & Insights

Analisis ini memungkinkan:

* Identifikasi aktor dengan pengaruh tinggi
* Pemahaman pola kolaborasi antar aktor
* Pembentukan komunitas dalam industri film
* Eksplorasi struktur jaringan yang kompleks

---

## 🚀 How to Run

1. Clone repository

```bash
git clone https://github.com/KurniaYufi/id-action-film-graph.git
```

2. Jalankan integrasi data

```bash
python merge-file.py
```

3. Import CSV ke Neo4j

4. Jalankan Graph Data Science

---

## 📌 Conclusion

Pendekatan integrasi data berbasis concatenation yang dikombinasikan dengan analisis graph memungkinkan eksplorasi relasi aktor–film secara lebih fleksibel. Meskipun tidak menggunakan entity matching yang kompleks, pendekatan ini efektif dalam memperkaya jaringan relasi dan mendukung analisis kolaborasi dalam industri film aksi Indonesia.

---

## 👩‍💻 Author

* Kurnia Yufi Satrio Laksono (5026231086)
* Muhammad Zaky Al Khair (5026231069)

---

Kalau kamu mau lebih “naik level” lagi buat nilai:

aku bisa bantu tambahin:

* 🔥 **limitasi metode kamu (kenapa concat itu ada kelemahan)**
* 🔥 **justifikasi kenapa tidak pakai entity resolution (biar dosen makin impressed)**
