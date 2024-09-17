# The Games Shop!
🔗 Link PWS: http://ahmad-dzulfikar31-ecomgames.pbp.cs.ui.ac.id/
## Tutorial Membuat Proyek django
#### Mengaktifkan Environment
1. Step pertama dari membuat projek django adalah membuat direktori di lokal terlebih dahulu, dan disini nama direktori saya adalah `eCom_Games` dan masuk kedalamnya menggunakan cd di terminal
2. Buatlah virtual environment
  ```
  python -m venv env
  ```
3. Nyalakan env-nya
  ```
   env\Scripts\activate
  ```
#### Membuat Projek django
4. Di dalam direktori tersebut buatlah file `requirements.txt` dan tambahkan depedencies berikut:
   django
  gunicorn
  whitenoise
  psycopg2-binary
  requests
  urllib3
5. Lakukan pip install untuk proyek tersebut!
   ```
   pip install -r requirements.txt
   ```
6. Buatlah proyek djangonya dengan nama bebas, nama project saya adalah `eCom_games`
## Tutorial Membuat aplikasi dengan nama `main` pada proyek
1. Pastikan sudah berada dalam direktori aplikasinya
2. Jalankan perintah
   ```
   python manage.py startapp main
   ```
## Tutorial Melakukan Routing Pada Proyek 
1. Buatlah berkas `urls.py` di dalam direktori main
2. Tambahkan route untuk request ke aplikasi `main` dengan tujuan menghubungkan "main" dan dapat dijalankan.
## Tutorial Membuat Model 
Bukalah models.py, lalu buatlah model dengan nama `Product` dan tambahkan atribut wajib seperti `name`, `price`, dan `description` beserta tipe datanya masing-masing. Ini memiliki tujuan untuk menyimpan data produk ke dalam database.
## Tutorial Membuat Sebuah Fungsi pada `views.py` untuk Dikembalikan ke Dalam Sebuah Template HTML
1. Didalam file `views.py` yang ada didalam `main` buatlah sebuah fungsi yang berguna untuk menerima parameter request dan fungsi tersebut akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
2. Ada sebuah dictionary yg berisikan data seperti `nama`, `harga`, dan `deskripsi` yang akan dikirim ke tampilan.
## Tutorial Membuat Sebuah Routing pada urls.py Aplikasi `main` untuk Memetakan Fungsi yang Dibuat di `views.py`
1. Buka `urls.py` di file `main`
2. Buat rute baru yang memetakan URL kedalam fungsi di `views.py` dengan tujuan memungkinkan pengguna untuk mengakses page dengan URL yang benar.
## Tutorial Melakukan Deployment ke PWS
1. Pertama, kita membuat project terlebih dahulu di PWS
2. Tambahkan URL deployment PWS pada `ALLOWED_HOSTS` di `settings.py`
3. Lakukan add, commit, dan push ke github
4. Lakukan git push ke pws dengan menjalankan perintah `git push pws main:master`
## Tutorial Membuat sebuah `README.MD`
Buatlah file `README.MD` yang bertujuan untuk menjelaskan alur dari apa yang sudah kita lakukan selama membuat proyek ini, langkah-langkah applikasi, dan tautan menuju deployment aplikasi.

## Bagan Request Client
![image](https://github.com/user-attachments/assets/e15bde03-197f-4236-a77e-1c3690d559b5)

## 💻 Fungsi Git
Git berfungsi sebagai sistem kontrol versi (Version Control System) yang memungkinkan pengembang perangkat lunak untuk melacak setiap perubahan kode secara terperinci. Git itu ibarat instagram untuk para programmer, dia bisa menyimpan semua dokumentasi dari kode yang kita buat, kita bisa melihat kode-kode orang lain, dan banyak lagi. Git juga mempermudah tim pengembang apat bekerja secara kolaboratif pada proyek yang sama, mengelola cabang (branch) yang berbeda untuk fitur baru, memperbaiki bug, dan menggabungkan perubahan (merge) dengan aman.

## ❓ Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Framework django sering dijadikan permulaan belajar perangkat lunak karna dapat dengan mudah dipahami oleh orang yang baru belajar perangkat lunak. Django juga menggunakan MVT yang dapat mempermudah pemula dapat memahami konsep dasar seperti routing, templating, dan manajemen database. Selain itu, django juga memiliki komunitas yang aktif dan dokumentasi lengkap yang dapat mempermudah pemula untuk lebih mengenal jauh dan belajar tentang perangkat lunak.

## 🔑 Mengapa model pada Django disebut ORM (Object-Relational Mapping)?
Model Django disebut Object Relational Mapping (ORM) karena Django memetakan model-model python ke dalam tabel-tabel dalam database dan membuat pengembang tidak perlu menulis kueri SQL secara langsung. Pengembang dapat dengan mudah mengakses dan memanipulasi data sehingga mempercepat proses pengembangan perangkat lunak.




