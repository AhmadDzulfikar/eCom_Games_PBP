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


# README.MD UNTUK TUGAS KE- 4
## Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
- `HttpResponseRedirect()`
  HttpResponseRedirect() adalah kelas yang secara langsung mengembalikan respons HTTP untuk melakukan redirect ke URL yang ditentukan. Contohnya seperti berikut:
  ```
  def login_user(request):
     if (request.user.is_authenticated):
          return redirect('main:show_main')
     
     if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
  
        if form.is_valid():
              user = form.get_user()
              login(request, user)
              response = HttpResponseRedirect(reverse('main:show_main'))
              response.set_cookie('last_login', datetime.datetime.now())
              return response
  
     else:
        form = AuthenticationForm(request)
  
     context = {'form': form}
     return render(request, 'auth/login.html', context)
  ```

  - `redirect()`
    redirect() adalah fungsi utilitas yang lebih tinggi yang menyederhanakan proses ini. redirect() juga lebih praktis karena bisa menerima parameter (URL, named URL patterns, dll) dan secara syntax lebih singkat. Contoh:
    ```
    # Authentication Views
    def register(request):
        form = UserCreationForm()
    
        if (request.method == "POST"):
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "User has been created")
                return redirect('main:login')
            
        context = {'form': form }
        return render(request, 'auth/register.html', context)
    ```

## Jelaskan cara kerja penghubungan model Product dengan User!
Dalam project django yang sedang saya buat, cara kerja model Product dengan User adalah lewat ForeignKey pada models dengan class Product. Jadi disini saat user membuat entri baru, entri yang dibuat hanya terhubung dengan tepat satu user yang login. Setiap User dapat memiliki banyak Product dan satu Product hanya bisa dimiliki oleh satu User. Contoh penggunaan sebagai berikut:
```
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
```

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
### Authentication
Proses untuk memverifikasi identitas pengguna. Ini melibatkan pemeriksaan apakah pengguna yang mencoba masuk ke sistem benar-benar adalah siapa yang mereka klaim. Contoh: Saat pengguna login dengan username dan password.

### Authorization
Setelah pengguna terautentikasi, otorisasi menentukan tingkat akses atau hak yang dimiliki pengguna tersebut dalam aplikasi. Ini adalah proses untuk mengontrol apa yang boleh atau tidak boleh dilakukan oleh pengguna. Contoh, jika dalam sebuah sistem web terdapat 2 role, yaitu admin, dan user, maka ketika pengguna login sebagai user dia memiliki fitur terbatas tidak dibanding admin.

### Apakah yang dilakukan saat pengguna login?
Saat melakukan login, authentication akan berjalan untuk mengecek apakah yanng pengguna yang mencoba masuk ini benar-benar role yang mereka klaim.
Lalu, Django akan memberikan authorization untuk memberikan dan membatasi sesuai dengan role yang didapat.

### Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Django memanfaatkan middleware untuk mengatur proses autentikasi dan otorisasi. User yang telah diotentikasi akan disimpan dalam objek request sebagai `request.user`. Ketika otorisasi, Django menggunakan sistem groups & permissions, yang dapat diatur.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan sesi (session) dan cookies. Ketika seorang pengguna login, Django membuat sesi baru yang menyimpan informasi pengguna, seperti ID pengguna. Informasi sesi ini biasanya disimpan di server, dan Django memberikan kepada pengguna sebuah cookie yang berisi ID sesi tersebut. Ketika pengguna mengunjungi halaman lain, cookie ini dikirim kembali ke server, memungkinkan Django untuk mengidentifikasi pengguna dan mengingat status login mereka.

### Kegunaan lain dari cookies
Dalam aplikasi e-commerce, cookies dapat menyimpan item yang ditambahkan ke keranjang belanja, memungkinkan pengguna untuk melanjutkan belanja mereka meskipun mereka meninggalkan situs.

### Apakah semua cookies aman digunakan?
Tidak semua cookies aman. Cookies dapat diserang seperti serangan XSS (Cross-Site Scripting) dan penyadapan data melalui koneksi yang tidak aman. Kita dapat mengatur cookies dengan atribut HttpOnly dan Secure untuk melindungi dari serangan-serangan tersebut.

## Implementasi Checklist
## Registrasi
a. Function dalam views untuk fitur registrasi
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
b. Tambahkan URL di urls.py
`path('register/', register, name='register'),`
c. dan buatlah sebuah html file di `main/templates/register.html'

## Login
a. Function dalam views untuk fitur registrasi
```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```
b. Tambahkan URL di urls.py
`path('login/', login_user, name='login'),`
c. dan buatlah sebuah html file di `main/templates/login.html'

## Logout
a. Function dalam views untuk fitur registrasi
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
b. Tambahkan URL di urls.py
`path('logout/', logout_user, name='logout'),`
c. dan buatlah sebuah button logout di `main/templates/main.html'
```
    <a href="{% url 'main:logout' %}">
        <button class="btn-logout">Logout</button>
    </a>
```


## Dua Akun, Tiga Dummy.
### Akun Pertama
![Screenshot 2024-09-24 225828](https://github.com/user-attachments/assets/986ba8a7-6e6a-46f6-b11f-8cc74b47a6a4)

## Akun Kedua
#![Screenshot 2024-09-24 230324](https://github.com/user-attachments/assets/d60b6a68-5b10-4d3a-b622-e2d012b8bc73)

## Menghubungkan model Product dengan User.
Menambahkan ForeignKey pada model Product, sehingga setiap produk yang sudah dibuat bisa dikaitkan ke pengguna.
```
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
```

## Menampilkan Detail Pengguna yang Sedang Login
USERNAME:
- Pertama kita harus memastikan kalau data last_loginnya yang ada di cookie dan usernamenya sudah terkirim
- ```
    user = form.get_user()
  login(request, user)
  response = HttpResponseRedirect(reverse('main:show_main'))
  response.set_cookie('last_login', datetime.datetime.now())
  return response
  ```

  - Kirim data last_loginnya ke show_main
  ```
  @login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name_owner': 'Ahmad Dzulfikar As Shavy',
        'class': 'PBP D',

        'title': request.user.username,
        'name': 'Flappy Box',
        'price' : '24',
        'Description': 'The game is inspired by',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
    ```
COOKIES:
- Cookies saat user sedang login di views.py
```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```
- Last Login `<h5>Sesi terakhir login: {{ last_login }}</h5>`

# README.MD UNTUK TUGAS KE- 5
## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1.) Inline Style, didefnisikan langsung pada elemen HTML menggunakan style. Contoh: `<div style="color: red;">Text here</div>`
2.) ID Selector, diterapkan menggunakan ID di HTML, contoh: 
```
#myId {
  color: blue;
}
```
`<div id="myId">Text here</div>`
3.) Class Selector, semua selector dengan simbol `.`, untuk pseudo seperti `:hover`, atau selector atribut seperti `[type="text"]`.
4.) Important Rule, dapat memberikan prioritas tertinggi untuk sebuah properti.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive itu sangat penting dalam mengembangkan aplikasi web karna itu menjamin agar tampilan yang sudah disusun rapih saat mengoding di web bisa terlihat rapih juga ketika kita membukanya di tablet, handphone, dan berbagai macam lainnya. Ini juga berguna agar programmer tidak harus membuat 2 jenis versi terpisah karna ketika sudah membuat yang di web kita juga dapat membukanya di handphone.

Contoh aplikasi yang sudah responsive: Bootstrap documentation, twitter
Contoh aplikasi yang belum responsive: Web yang dibuat ketika aplikasi mobile belum menjadi tren.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin: 
Margin adalah sebuah ruang kosong di luar dari border yang berguna untuk jarak antara elemen-elemen yang ada di web.
```
.box {
  margin: 20px;  /* naIni berguna untuk menambahkan margin 20 piksel di semua sisi elemen */
}
```

Border:
Border adalah garis yang mengelilingi elemen, diantara margin dan padding. Border dapat dihias seperti diberi warna, lebar, dll.
```
.box {
  border: 2px solid black;  /* Border dengan lebar 2 piksel, jenis solid, dan warna hitam */
}
```

Padding
Padding adalah ruang di dalam elemen antara konten dengan border dengan tujuan untuk memberi jarak agar konten tidak menempel langsung dengan batasnya.
```
.box {
  padding: 15px;  /* Menambahkan padding 15 piksel di semua sisi elemen */
}
```

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box
Flexbox adalah modul CSS yang dirancang untuk mengatur tata letak elemen dalam satu dimensi—baik secara horizontal (baris) atau vertikal (kolom). Flexbox berguna untuk membuat tata letak satu dimensi, seperti navbar, baris produk, tombol yang tersusun dalam satu baris, atau komponen-komponen kecil lainnya.

Grid layout
Grid Layout adalah sistem tata letak yang lebih kompleks dan memungkinkan pengaturan tata letak elemen dalam dua dimensi (baris dan kolom). Kegunaan grid layout untuk membuat tata letak dua dimensi, seperti layout halaman penuh yang memiliki struktur lebih kompleks, misalnya header, sidebar, konten utama, dan footer.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
### 1. Implementasikan fungsi untuk menghapus dan mengedit product.
1. Seperti sebelum-sebelumnya, kalau mau menambahkan fitur baru kita harus membuatnya di `views.py`. Buatlah fungsi baru untuk edit dan delete seperti ini:
Edit:
```
def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

Delete:
```
def delete_product(request, id):
    # Get mood berdasarkan id
    mood = Product.objects.get(pk = id)
    # Hapus mood
    mood.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Setelah membuat fungsi untuk kedua fitur tersebut, selanjutnya kita membuat file html untuk edit yang berguna sebagai tempat atau halaman edit bekerja. Buatlah `create_product.html`.
3. Tambahkan mereka di `urls.py`, pertama tambahkan import mereka `from main.views import edit_product` & `from main.views import delete_product`, lalu tambahkan mereka di `url_patterns`:
```
urlpatterns = [
...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
]
```

### Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
Hal yang saya lakukan untuk mengedit halaman login, register, dan tambah product adalah menyalin dari tutorial 😁😁😁 dan saya ubah sedikit untuk menyesuaikan dengan tema dari toko saya, yaitu toko game. Saya mengubah warna background dari halaman-halaman tersebut ke warna gelap dan mengubah warna font menjadi hijau terang untuk memberikan kesan neon.
Login:
![image](https://github.com/user-attachments/assets/e847b882-ec1e-4f4c-99e2-e02429f9ee28)

Register:
![image](https://github.com/user-attachments/assets/de070e54-b2bd-41de-a64b-c37dfeaae909)

Tambah Product:
![image](https://github.com/user-attachments/assets/9de30b92-f35c-401c-978c-e471757dbbf4)

### Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
Cara saya mengimplementasikan hal ini yaitu menampilkan gambar ketika product kosong adalah dengan if else yang berjalan dengan ketentuan berikut: Jika bukan product maka munculkan image, selain itu maka munculkan card product
```
<div class="container">
    {% if not products %}
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
            <p class="text-center text-gray-600 mt-4">Belum ada produk yang tersedia saat ini.</p>
        </div>
    {% else %}
        <div class="product-grid">
            {% for product in products %}
                {% include 'card_product.html' %}
            {% endfor %}
        </div>
    {% endif %}
</div>
```
Jika product kosong maka munculkan image:
![image](https://github.com/user-attachments/assets/cc37e1cc-6c5c-4345-a020-5260379242f8)

Jika product tersedia:
![image](https://github.com/user-attachments/assets/189002f8-c8c2-4b33-9381-772f2ae5a05c)

### Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
Untuk mengimplementasikan hal tersebut saya harus memasukkan button edit dan button delete kedalam card agar setiap card memiliki kedua button tersebut:
```
<div class="product-card">
    <h3>{{ product.name }}</h3>
    <p class="price">${{ product.price }}</p>
    <p>{{ product.description }}</p>
    <a href="{% url 'main:edit_product' product.pk %}">
        <button class="btn-action">
            Edit
        </button>
    </a>
    <a href="{% url 'main:delete_product' product.pk %}">
        <button class="btn-action">
            Delete
        </button>
    </a>
</div>
```
Contoh Implementasi:
![image](https://github.com/user-attachments/assets/4eeef40f-90a8-49f9-b4b7-00684c7c692f)

### Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
Saya mencari contoh navigation bar di google dan langsung implementasikan di proyek saya, https://flowbite.com/docs/components/navbar/. Dalam navigation bar yang saya pilih dan saya implementasikan, ini sudah responsive terhadap mobile atau apapun device selain laptop, contoh implementasi:
Tampilan di laptop:
![image](https://github.com/user-attachments/assets/7fb60c9e-380a-443e-a976-97b70c14401a)

Tampilan di iPhone XR:


![image](https://github.com/user-attachments/assets/7e0e7cc4-2f53-450e-9d54-3488abbd9c7c)

Navbar jika di buka:

![image](https://github.com/user-attachments/assets/aed18f18-bae2-4672-b1e0-74a2d44c5a81)

# README.MD UNTUK TUGAS KE- 6
##  Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Dalam pengembangan aplikasi web, javascript dapat membuat website jauh lebih menarik, interaktif, dan dinamis. Contohnya adalah konten yang bergerak dan memperbarui secara real-time tanpa perlu reload semua halaman website berkali-kali.  Sebagai contoh, Google Maps dengan user experience yang sangat baik. Javascript membuat website menjadi lebih hidup.

## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Dalam sisi callback, `await` dapat digunakan untuk membuat penanganan asynchronus lebih mudah dibaca dan di-maintain karena menulis kode secara sekuensial. `fetch()` mengirimkan permintaan HTTP ke server dan mengembalikan sebuah promise. Dengan menambahkan await di depan `fetch()`, JavaScript menunggu hingga promise tersebut selesai (baik berhasil maupun gagal) sebelum melanjutkan ke baris kode berikutnya.

Jika await tidak digunakan maka Javascript tidak menunggu respons dari `fetch()` dan dia akan langsung mengeksekusi baris kode selanjutnya. Hal ini menyebabkan data yang diminta mungkin belum tersedia ketika Anda mencoba mengaksesnya, yang dapat menimbulkan error seperti `undefined` atau `Promise {<pending>}`.

##  Mengapa kita perlu menggunakan _decorator_ `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?
Token csrf berguna untuk menjamin kalau permintaan yang kita kirim ke server sudah berasal dari tempat yang sah, karena django memiliki perlindungan CSRF secara default untuk mencegah serangan di mana pengguna yang terotentikasi di sebuah web disalahgunakan untuk mengirim permintaan ke server tanpa sepengetahuan mereka. Decorator `@csrf_exempt` memberi tahu Django untuk menonaktifkan pemeriksaan CSRF pada view tertentu.

##  Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Jika hanya ada validasi di frontend, server tetap rentan terhadap serangan seperti **injection attacks** (misalnya, SQL injection atau XSS). Backend bertanggung jawab untuk memastikan bahwa data yang diterima adalah valid dan sesuai dengan standar aplikasi. Jika pembersihan hanya dilakukan di frontend, tidak ada jaminan bahwa data yang sampai di backend sudah benar-benar bersih dan aman, sehingga bisa terjadi korupsi data di database.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!













