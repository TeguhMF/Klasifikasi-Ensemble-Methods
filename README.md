# Klasifikasi: Ensemble Methods
---
## Kelompok 5
- Della Nanda Saputri      2412011401352
- Nurhidayat               241011401624
- Nur Rizka Sasi Kirana    241011401355
- Teguh Maulana Firmansyah 241011401348
- Yose Alfredow Panjaitan  241011402036
---
Video Persentasi : https://youtu.be/DLV9PxbVSBM?si=zfwv9OX89CNC7vVK
code dan output  : https://colab.research.google.com/drive/15CFvxLWxHOEQZEys5Sk9E9rR0hUA1IoV?usp=sharing

Pernah dengar pepatah **"dua kepala lebih baik dari satu"**? Ternyata prinsip ini juga berlaku di dunia data mining. Daripada mengandalkan satu model untuk membuat prediksi, mengapa tidak menggabungkan kekuatan beberapa model sekaligus? Inilah ide dasar dari **Ensemble Methods**, salah satu teknik klasifikasi yang terbukti mampu menghasilkan prediksi lebih akurat dan stabil dibandingkan model tunggal.

Bayangkan kamu sedang menebak hasil pertandingan sepak bola. Satu orang bisa saja salah prediksi karena bias atau informasi yang terbatas. Namun jika kamu bertanya kepada seratus orang dan mengambil suara terbanyak, hasilnya biasanya lebih mendekati kenyataan. Analogi *wisdom of the crowd* inilah yang menjadi fondasi mengapa ensemble learning bekerja sangat efektif dalam machine learning.

Dalam dunia data mining, terdapat beberapa pendekatan ensemble yang populer, seperti **Bagging** (Random Forest), **Boosting** (AdaBoost, XGBoost, LightGBM), **Stacking**, dan **Voting**. Masing-masing memiliki strategi berbeda dalam mengombinasikan model, tetapi tujuan utamanya sama, yaitu mengurangi error sehingga model menjadi lebih andal ketika menghadapi data baru.

---

## Apa Itu Ensemble Learning?

**Ensemble Learning** merupakan metode yang menggabungkan beberapa model (*base learner*) untuk menghasilkan prediksi yang lebih baik dibandingkan menggunakan satu model saja.

Konsepnya mirip seperti meminta pendapat dari beberapa orang sebelum mengambil keputusan. Setiap model akan memberikan prediksi, kemudian seluruh hasil tersebut digabungkan untuk menghasilkan prediksi akhir yang lebih akurat dan stabil.

---

## Mengapa Ensemble Lebih Baik?

Ensemble Methods sering dianggap lebih baik karena menerapkan konsep **Wisdom of the Crowd** atau kebijaksanaan dari banyak pendapat.

Jika hanya mengandalkan satu model, kemungkinan terjadinya kesalahan masih cukup besar. Namun ketika beberapa model digabungkan, kesalahan dari satu model dapat dikoreksi oleh model lainnya.

Agar ensemble bekerja dengan baik, terdapat dua syarat utama:

1. Setiap model harus memiliki akurasi yang cukup baik atau lebih baik daripada tebakan acak.
2. Model-model tersebut harus memiliki keragaman (*diversity*) sehingga menghasilkan kesalahan yang berbeda-beda.

Dengan demikian, tingkat kesalahan keseluruhan dapat menjadi lebih kecil dibandingkan model individual.

---

## Jenis-Jenis Ensemble Methods

### 1. Bagging (Bootstrap Aggregating)

Bagging bertujuan mengurangi **variance** dan risiko **overfitting** dengan melatih beberapa model menggunakan sampel data yang berbeda.

**Contoh:** Random Forest

### 2. Boosting

Boosting berfokus memperbaiki kesalahan model sebelumnya secara bertahap sehingga dapat mengurangi **bias**.

**Contoh:**

- AdaBoost
- XGBoost
- LightGBM

### 3. Stacking

Stacking menggabungkan beberapa model menggunakan model tambahan (*meta-learner*) untuk memperoleh hasil prediksi yang lebih optimal.

### 4. Voting

Voting menggabungkan hasil prediksi dari beberapa model melalui mekanisme pemungutan suara (*voting*).

---

## Kelebihan dan Kekurangan Ensemble Methods

### Kelebihan

- Meningkatkan akurasi prediksi.
- Mengurangi risiko overfitting.
- Lebih stabil terhadap variasi data.
- Mampu menangani dataset yang besar dan kompleks.

### Kekurangan

- Waktu pelatihan lebih lama.
- Membutuhkan memori lebih besar.
- Interpretasi model lebih sulit dibandingkan model tunggal.
- Implementasi relatif lebih kompleks.

Meskipun demikian, peningkatan performa yang diperoleh sering kali sebanding dengan kompleksitas yang ditambahkan.

---

## Contoh Penerapan Ensemble Methods

Ensemble Methods telah banyak diterapkan di berbagai bidang, antara lain:

### Kesehatan
Memprediksi penyakit berdasarkan data pasien.
### Keuangan
Mendeteksi transaksi fraud atau penipuan.
### Pendidikan
Memprediksi tingkat kelulusan mahasiswa.
### Perbankan
Menganalisis kelayakan pemberian kredit.
### E-Commerce
Mengembangkan sistem rekomendasi produk yang lebih akurat.

---

## Bagging (Bootstrap Aggregating)

Bagging merupakan salah satu metode ensemble yang paling populer.

### Cara Kerja

1. Membuat beberapa sampel bootstrap dari data training menggunakan teknik *sampling with replacement*.
2. Setiap sampel digunakan untuk melatih satu model Decision Tree.
3. Ketika ada data baru yang diprediksi, seluruh model memberikan hasil prediksinya.
4. Hasil akhir ditentukan menggunakan:
   - **Majority Voting** untuk klasifikasi.
   - **Rata-rata prediksi** untuk regresi.

Metode ini dapat meningkatkan stabilitas model dan mengurangi risiko overfitting.

---

## Random Forest: Perbaikan dari Bagging

Random Forest merupakan pengembangan dari Bagging.

Jika pada Bagging setiap Decision Tree menggunakan seluruh fitur yang tersedia, maka pada Random Forest setiap node hanya mempertimbangkan sebagian fitur yang dipilih secara acak.

Pendekatan ini membuat setiap tree menjadi lebih beragam sehingga korelasi antar tree menjadi lebih rendah dan error keseluruhan model dapat berkurang.

### Keunggulan Random Forest

- Tidak mudah overfitting.
- Mampu menangani data berdimensi tinggi.
- Menyediakan informasi pentingnya fitur (*feature importance*).
- Robust terhadap outlier.

---

## Konsep Dasar Boosting

Berbeda dengan Bagging yang melatih model secara paralel, Boosting melatih model secara bertahap (*sequential*).

Setiap model baru akan fokus memperbaiki kesalahan yang dibuat oleh model sebelumnya.

### Kelebihan

- Efektif mengurangi bias.
- Meningkatkan performa prediksi.

### Kekurangan

- Risiko overfitting lebih tinggi apabila tidak dikontrol dengan baik.

---

## Alur Implementasi Ensemble Methods

1. Menyiapkan dataset.
2. Melakukan preprocessing data.
3. Membagi data menjadi training dan testing.
4. Melatih model ensemble (Random Forest, AdaBoost, XGBoost, dan lainnya).
5. Melakukan prediksi terhadap data testing.
6. Mengevaluasi hasil menggunakan:
   - Accuracy
   - Precision
   - Recall
   - F1-Score
   - Confusion Matrix
7. Membandingkan performa model ensemble dengan model tunggal.

---

## Kode Python Bagian 1 dan 2

Pada bagian ini dilakukan:

- Import library yang dibutuhkan.
- Membaca dataset.
- Melakukan preprocessing data.
- Membagi data training dan testing.
- Melatih model ensemble.

Tahapan ini menjadi dasar agar model dapat belajar dari data yang tersedia sebelum digunakan untuk melakukan prediksi.

<img width="1303" height="654" alt="image" src="https://github.com/user-attachments/assets/7f3e9a76-ac1d-4b56-94ed-64b6f451a538" />
<img width="1211" height="707" alt="image" src="https://github.com/user-attachments/assets/b213220b-964d-4c4f-b6b4-04ca3eabb6a6" />
<img width="1064" height="687" alt="image" src="https://github.com/user-attachments/assets/76c4debd-8a5a-40d0-8c03-888fbd9f4aa5" />





---

## Kode Python Bagian 3 dan 4

Pada bagian ini dilakukan:

- Prediksi menggunakan model yang telah dilatih.
- Evaluasi performa model menggunakan berbagai metrik evaluasi.
- Analisis hasil klasifikasi.

Melalui evaluasi tersebut dapat diketahui apakah model ensemble memberikan hasil yang lebih baik dibandingkan model tunggal.

---

## Kesimpulan

Ensemble Methods merupakan teknik dalam data mining yang menggabungkan beberapa model pembelajaran untuk menghasilkan prediksi yang lebih akurat dan stabil dibandingkan menggunakan satu model saja.

Metode seperti **Bagging**, **Random Forest**, dan **Boosting** memiliki pendekatan yang berbeda dalam meningkatkan performa model, baik dengan mengurangi variance maupun bias.

Karena kemampuannya dalam meningkatkan akurasi dan ketahanan model terhadap berbagai kondisi data, Ensemble Methods banyak digunakan dalam bidang kesehatan, keuangan, pendidikan, dan e-commerce untuk mendukung pengambilan keputusan yang lebih baik.

---

## Penutup

Sampai di sini, kita telah mempelajari bagaimana Ensemble Methods bekerja, mulai dari konsep dasarnya, jenis-jenisnya seperti Bagging, Boosting, Stacking, dan Voting, hingga implementasi dan penerapannya dalam berbagai bidang.

Pada akhirnya, Ensemble Methods mengajarkan satu hal penting dalam dunia data mining: **kolaborasi sering kali mengungguli individualitas**. Sebagaimana keputusan yang diambil bersama cenderung lebih bijaksana, model-model yang saling melengkapi juga dapat menghasilkan prediksi yang lebih akurat dan tangguh dibandingkan mengandalkan satu model saja.

Semoga materi ini dapat menambah wawasan mengenai salah satu teknik klasifikasi yang banyak digunakan dalam Data Mining.

---

## Referensi

1. Witten, I. H., Frank, E., Hall, M. A., & Pal, C. J. *Data Mining: Practical Machine Learning Tools and Techniques*.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. *An Introduction to Statistical Learning*.
3. Scikit-Learn Documentation — Ensemble Methods.
4. Dr. Arya Adhyaksa, W. *Modul DM06: Klasifikasi - Ensemble Methods*.

---
