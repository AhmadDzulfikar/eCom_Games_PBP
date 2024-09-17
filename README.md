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

# README.MD UNTUK TUGAS KE-3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Platform bertindak sebagai fondasi untuk berbagai aplikasi, perangkat, atau apapun layanan yang digunakan oleh user, oleh karena itu data delivery digunakan untuk pengimplementasiannya. Platform biasanya terdiri dari database, server, frontend, dan data delivery memungkinkan komunikasi antar komponen ini, sehingga informasi yang dihasilkan oleh satu elemen dapat diteruskan dengan tepat ke elemen lainnya.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya lebih baik JSON dibandingkan dengan XML dengan berbagai macam alasan. Alasan pertama adalah struktur data dari JSON lebih lebih sederhana dan lebih mudah kebaca, sebagai contoh:
JSON:
```
{
    "name": "John",
    "age": 30
}
```

XML:
```
<person>
    <name>John</name>
    <age>30</age>
</person>
```
Selain itu, karena JSON tidak menggunakan tag penutup dan sintaksnya lebih sederhana, JSON biasanya menghasilkan payload yang lebih kecil dari XML. Alasan mengapa JSON lebih populer dan lebih banyak digunakan ketimbang XML adalah karena lebih ringan, lebih cepat diproses, dan lebih mudah digunakan dalam pengembangan web dan aplikasi mobile.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid` sangat penting dalam proses validasi form sebelum data disimpan atau diproses lebih lanjut. Salah satu fungsi dari `is_valid` adalah memeriksa validitas data saat form dikirimkan, data input dari pengguna harus diperiksa apakah sesuai dengan aturan validasi yang diterapkan pada masing-masing field. Kita sangat membutuhkan method `is_valid` dengan berbagai alasan seperti mencegah error pada level aplikasi, validasi data sebelum pemrosesan, dan memudahkan penanganan error.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

### Mengapa kita membutuhkan csrf_token saat membuat form di Django?
Dengan `csrf_token` kita dapat melindungi dari serangan CSRF karena `csrf_token` membantu memverifikasi bahwa permintaan yang dikirim dari klien benar-benar berasal dari sumber yang sah.

### Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?
Pengguna Tidak Sengaja Mengirimkan Permintaan Berbahaya Penyerang dapat membuat pengguna mengunjungi halaman web berbahaya yang berisi skrip atau form tersembunyi yang otomatis mengirimkan permintaan ke aplikasi tanpa sepengetahuan pengguna. Contohnya, jika aplikasi web memiliki endpoint untuk menghapus akun atau mentransfer dana, penyerang dapat membuat permintaan POST ke endpoint tersebut.

### Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Penyerang dapat membuat halaman web atau email yang mengandung skrip atau elemen tersembunyi yang mengirimkan permintaan berbahaya. Misalnya, dengan menggunakan tag HTML seperti <img>, penyerang dapat memaksa browser korban untuk melakukan permintaan POST ke server target.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1.) Hal pertama yang saya lakukan adalah membuat direktori `templates` di direktori utama dan membuat berkas HTML baru bernama `base.html`
2.) Setelah membuat direktori templates baru, saya langsung mendaftarkan direktori templates tersebut ke `settings.py`
### 3.) Membuat Input Form
Dalam membuat form input data, saya membuat file py baru bernama `forms.py` di direktori `main` dengan isi sebagai berikut:
```
from django.forms import ModelForm
from main.models import MoodEntry

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["mood", "feelings", "mood_intensity"]
```
Lalu membuat fungsi dengan nama `create_product` di halaman `views.py` dengan isi sebagai berikut:
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
Lalu tambahkan path url ke dalam variable `urlpatterns` di `urls.py` di `main`.
```
urlpatterns = [
   ...
   path('create-mood-entry', create_mood_entry, name='create_mood_entry'),
]
```
Lalu membuat berkas HTML baru untuk templates yang berguna untuk mengirim request ke view 
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Mood Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Mood Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
Terakhir, tambahkan `{% block content %}` di main.html
### 4.) Menambahkan 4 fungsi `views`
#### a.) Format XML
Import `HttpResponse` dan `serializers` di `views.py`
```
from django.http import HttpResponse
from django.core import serializers
```
Buatlah fungsi baru yang bertugas untuk menerima parameter request
```
def show_xml(request):
    data = MoodEntry.objects.all()
```
Tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query
```
def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
#### b.) Format JSON
Buat fungsi `show_json` di dalam `views.py` yang ada di direktori `main` yang berfungsi menyimpan hasil query.
```
def show_json(request):
    data = Product.objects.all()
```
Tambahkan function berupa `HttpResponse` 
```
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
#### b.) Format XML by ID & JSON by ID
Buatlah fungsi baru yang menerima parameter request dan id di `views.py`
### XML
```
def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

### JSON
```
def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Tambahkan import pada `urls.py` di direktori `main`
`from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id`

dan tambahkan path URL di `urlpatterns` 
```
...
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
...
```

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
### XML ALL
![Screenshot 2024-09-17 185207](https://github.com/user-attachments/assets/66c53361-54d0-4480-b521-56f8f8051c81)

### JSON ALL
![Screenshot 2024-09-17 185022](https://github.com/user-attachments/assets/8d389f70-058d-4735-b3be-501f69999ee4)

### XML by ID
![Screenshot 2024-09-17 185300](https://github.com/user-attachments/assets/2c9671c5-739a-4167-b40a-f5456d904b27)

### JSON by ID
![Screenshot 2024-09-17 185348](https://github.com/user-attachments/assets/a2f89f61-2df4-4432-818d-618c06e0b228)














