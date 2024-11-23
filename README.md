# Laporan Pertama Penerapan Sains Data - andrymldni

## Domain Project
>Menyelesaikan permasalahan human resources di perusahaan Jaya Jaya Maju

  <p align="center">
  <img src="https://github.com/user-attachments/assets/1a48f5cf-40d9-457e-904f-e6b689835f3f" alt="HR" width="500">
  </p>


## Business Understanding
Jaya Jaya Maju adalah sebuah perusahaan multinasional yang didirikan pada tahun 2000 dan kini telah memiliki lebih dari 1000 karyawan yang tersebar di seluruh negeri. Meskipun perusahaan ini telah berkembang menjadi entitas bisnis yang besar, Jaya Jaya Maju masih menghadapi tantangan signifikan dalam mengelola karyawannya. Salah satu masalah utama yang dihadapi adalah tingginya tingkat pergantian karyawan (attrition rate) yang mencapai lebih dari 10%. Tingginya tingkat pergantian karyawan ini menunjukkan adanya masalah dalam manajemen sumber daya manusia, yang mungkin mencakup kepuasan kerja, keseimbangan kehidupan kerja, pengembangan karir, atau budaya organisasi. Masalah ini tidak hanya berdampak pada produktivitas dan efisiensi operasional perusahaan, tetapi juga menimbulkan biaya tambahan terkait rekrutmen dan pelatihan karyawan baru, serta berpotensi mengganggu stabilitas dan keberlanjutan bisnis Jaya Jaya Maju di masa depan.

Jika tingkat pergantian karyawan ini terus meningkat, perusahaan dapat menghadapi beberapa konsekuensi serius. Pertama, biaya yang dikeluarkan untuk rekrutmen dan pelatihan karyawan baru akan terus meningkat, menguras sumber daya finansial yang seharusnya dapat digunakan untuk pengembangan bisnis atau inovasi. Kedua, seringnya pergantian karyawan dapat mengganggu kontinuitas dan konsistensi operasional, yang berpotensi menurunkan kualitas layanan atau produk yang dihasilkan. Hal ini dapat berdampak negatif pada reputasi perusahaan di mata pelanggan dan mitra bisnis.

Selain itu, tingginya attrition rate dapat menimbulkan dampak jangka panjang yang lebih serius, seperti menurunnya moral dan semangat kerja di kalangan karyawan yang masih bertahan. Mereka mungkin merasa tidak aman dalam pekerjaan mereka atau kehilangan kepercayaan pada manajemen perusahaan. Jika situasi ini tidak segera diatasi, perusahaan dapat mengalami kesulitan dalam menarik talenta baru yang berkualitas, karena calon karyawan mungkin melihat perusahaan sebagai tempat kerja yang tidak stabil. Dalam jangka panjang, hal ini bisa menghambat pertumbuhan dan perkembangan Jaya Jaya Maju, mengurangi daya saingnya di pasar, dan akhirnya mengancam kelangsungan bisnisnya.

## Problem Statements
Bagaimana Jaya Jaya Maju dapat menurunkan tingkat pergantian karyawan untuk meningkatkan produktivitas, efisiensi, dan stabilitas bisnis? Masalah ini mencakup beberapa aspek penting:

- Faktor utama penyebab tingginya turnover karyawan.
- Pengaruh kepuasan kerja, keseimbangan kerja-hidup, peluang karir, dan budaya organisasi terhadap retensi karyawan.
- Strategi manajemen untuk meningkatkan kepuasan dan retensi karyawan.
- Praktik terbaik dalam manajemen sumber daya manusia yang relevan untuk mengurangi tingkat pergantian karyawan.

## Project Scope

1. Melakukan analisis kebutuhan perusahaan yang mencakup tahapan berikut.
   - **Pemahaman Bisnis** (Busness Understanding)
   - **Pemahaman Data** (Data Understanding)
2. Membangun model yang terdiri dari langkah-langkah berikut.
   - **Persiapan Data** (Data Preparation)
   - **Pembuatan Model** (Modeling)
   - **Evaluasi Model** (Model Evaluation)
   - **Pembuatan Dashboard**
3. Memanfaatkan model yang telah dikembangkan untuk memprediksi data baru, menggunakan model dengan hasil evaluasi terbaik.

## Persiapan
Informasi dataset dapat dilihat pada tabel dibawah ini.

Jenis | Keterangan
--- | ---
Sumber | [Dicoding : employee_data ](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)
Lisensi | Dicoding Academy
Kategori | Employment, Business
Jenis dan Ukuran Berkas | CSV (221 KB)

Dataframe ini memiliki 1471 baris dan 35 kolom.

### Notebook
1. Data Understanding memahami dataset yang akan digunakan
2. Data Preparation / Preprocesing
   - mengimport dataset ke dalam notebook
   - melakukan eksplorasi data dan memahami struktur, pola, dan statistik penting pada data
   - identifikasi atribut-atribut yang mungkin berperan penting dalam pembentukan model machine learning
3. Encoder atribut dengan standardsclaer dan ordinalencoder
   - identifikasi atribut yang memerlukan standardscaler, terutama untuk atribut kategorical yang perlu diubah ke numerik
   - menggunakan fitur encoder seperti `StandardScaler` dan `OrdinalEncoder` dari scikit-learn
4. Membuat model dengan logistic regression
   - pisahkan data menjadi data train dan data test 80:20
   - membuat model logistic regression dari scikit-learn
   - latih model menggunakan data pelatihan
   - mengevaluasi kinerja model
   - cek fitur importance dari model yang terbentuk
   - simpan model dan encoder
5. Membuat code sederhana untuk melakukan prediction
   

### Menjalankan File Prediction.py
1. Buka IDE favorit kamu
2. Jalankan perintah berikut
   ```
    pip install requirements.txt
   ```
   kode diatas untuk menginstall dependensi yang digunakan dalam proyek ini
3. Buka file prediction.py
4. pastikan `lr_model.pkl` berada di folder yang sama
5. Jalankan file prediction.py
6. Tunggu hingga muncul ouput hasil prediksi
7. Selesai

### Pembuatan Dasboard menggunakan Metabase
1. Ekspor ke superbase
   ```
   from sqlalchemy import create_engine
   URL = "postgresql://postgres.xmkorqdrdzuuqziprgxf:XSma7DXcyHTUIJ50@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

   engine = create_engine(URL)
   reshape_df.to_sql('Clean_employee.csv', engine)
   ```
   ```
   Host: aws-0-ap-southeast-1.pooler.supabase.com
   Database name: postgres
   Port: 6543
   User: postgres.xmkorqdrdzuuqziprgxf
   ```

## Sturktur File

```

📦Submission-1
 ┣ 📜andrymldni-Dashboard.png
 ┣ 📜andrymldni.mp4
 ┣ 📜clean_employee.csv
 ┣ 📜lr_model.pkl
 ┣ 📜metabase.db.mv.db
 ┣ 📜notebook benar.ipynb
 ┣ 📜prediction.py
 ┣ 📜Readme.md
 ┗ 📜requirements.txt

```

## Business Dashboard
Dashboard ini memberikan gambaran yang jelas tentang berbagai faktor yang memengaruhi retensi tenaga kerja di Jaya Jaya Maju. Dengan informasi yang diperoleh, perusahaan dapat merumuskan strategi berbasis data untuk meningkatkan kepuasan karyawan, mengurangi attrition, dan mendukung pertumbuhan jangka panjang.

![andrymldni-Dashboard](https://github.com/user-attachments/assets/e02d09a4-4e90-47b9-b053-f35df5ce04f5)

## Conclusion
Berdasarkan data yang dianalisis, dapat disimpulkan bahwa faktor-faktor demografis dan pekerjaan memiliki peran signifikan dalam mempengaruhi tingkat pergantian karyawan di perusahaan. Sebagian besar karyawan yang keluar berasal dari departemen tertentu, dengan tingkat attrition yang lebih tinggi di antara karyawan dengan latar belakang pendidikan teknik dan peran pekerjaan tertentu, seperti Sales Representative. Faktor lain yang berkontribusi pada pergantian karyawan termasuk status pernikahan, dengan karyawan yang berstatus single cenderung memiliki tingkat attrition yang lebih tinggi. Selain itu, meskipun tidak ada perbedaan yang signifikan antara gender, aspek lain seperti kepuasan kerja, keseimbangan kehidupan kerja, dan pengembangan karir dapat mempengaruhi keputusan karyawan untuk tetap bertahan di perusahaan. Oleh karena itu, penting bagi manajemen untuk mengembangkan strategi yang berfokus pada peningkatan kepuasan kerja, menawarkan peluang pengembangan karir, dan menciptakan budaya kerja yang mendukung keseimbangan kehidupan kerja guna mengurangi tingkat pergantian karyawan dan meningkatkan retensi di masa depan.

## Action Recommendations
1. Berdasarkan analisis masalah yang telah disajikan, beberapa strategi untuk meningkatkan kepuasan dan retensi karyawan antara lain:
   - Menciptakan lingkungan kerja yang mendukung dengan mendengarkan masukan karyawan dan membangun budaya yang inklusif.
   - Menyediakan peluang pengembangan karir dan pelatihan yang berkelanjutan.
   - Memberikan kenaikan gaji yang kompetitif dan insentif untuk meningkatkan motivasi dan loyalitas.
   - Mengurangi beban kerja berlebih dan memastikan keseimbangan antara pekerjaan dan kehidupan pribadi untuk mengurangi stres dan kelelahan.

2. Untuk manajemen sumber daya manusia, beberapa praktik terbaik yang dapat diterapkan meliputi:
   - Melakukan survei kepuasan karyawan secara rutin untuk mengidentifikasi area perbaikan.
   - Menerapkan program kesejahteraan yang mencakup fleksibilitas kerja, dukungan kesehatan mental, dan keseimbangan kehidupan kerja.
   - Meningkatkan komunikasi terbuka antara manajemen dan karyawan guna memperkuat keterlibatan dan kepercayaan.
   - Mendukung kolaborasi dan pengembangan profesional melalui program mentorship dan pembentukan tim yang solid.

Dengan mengimplementasikan langkah-langkah ini, Jaya Jaya Maju dapat menurunkan tingkat pergantian karyawan, serta meningkatkan produktivitas, efisiensi, dan stabilitas bisnis di masa depan.
