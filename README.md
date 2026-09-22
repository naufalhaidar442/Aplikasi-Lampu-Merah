# Aplikasi Traffic Light — Tugas Besar PBO

## Anggota Kelompok
| No |             Nama            |   NIM   |
|----|-----------------------------|---------|
| 1  | Naufal Haidar Putera Syarif | 2511032 |
| 2  |      |     |
| 3  |      |     |
| 4  |      |     |

## Deskripsi

Program ini adalah simulasi **Traffic Light** (lampu lalu lintas) sederhana yang berjalan di terminal. Lampu berganti warna secara otomatis dengan jeda **5 detik** setiap pergantian, mengikuti urutan:

```
HIJAU → MERAH → KUNING → HIJAU → ...
```

Program ditulis menggunakan **Python** dan menerapkan konsep **Pemrograman Berorientasi Objek (PBO/OOP)**.

## Requirement

- Python 3.x
- Tidak memerlukan library eksternal tambahan (hanya menggunakan `time` dan `abc` yang merupakan bagian dari Python standard library)
- Disarankan dijalankan di terminal yang mendukung ANSI escape code (Command Prompt modern, PowerShell, Terminal Linux/Mac) agar warna tampil dengan benar

## Cara Menjalankan

```bash
python index.py
```

atau

```bash
python3 index.py
```

Program akan berjalan terus-menerus (`while True`) sampai dihentikan manual dengan `Ctrl + C`.

## Struktur File

| File | Keterangan |
|------|------------|
| `index.py` | Source code utama aplikasi Traffic Light |
| `README.md` | Dokumentasi tugas ini |

## Konsep OOP yang Diterapkan

Program ini menerapkan **kelima pilar OOP** sekaligus:

### 1. Class & Object
Program terdiri dari 5 class: `Lampu`, `LampuMerah`, `LampuKuning`, `LampuHijau`, dan `TrafficLights`. Objek utama yang dijalankan adalah `LampuLaluLintas = TrafficLights()`.

### 2. Encapsulation (Enkapsulasi)
Atribut `_CurrentLight` dibuat protected (diawali underscore) dan tidak diakses langsung dari luar class. Akses dilakukan melalui **property** `Current_Light` yang memiliki validasi di dalam setter-nya:

```python
@Current_Light.setter
def Current_Light(self, value):
    if value not in ["MERAH", "HIJAU", "KUNING"]:
        raise ValueError("Warna tidak sesuai!")
    self._CurrentLight = value
```

Validasi ini mencegah nilai warna yang tidak valid disimpan ke dalam objek.

### 3. Inheritance (Pewarisan)
Class `LampuMerah`, `LampuKuning`, dan `LampuHijau` masing-masing **mewarisi** (inherit) dari class dasar `Lampu`:

```python
class LampuMerah(Lampu):
    ...
```

Ketiga class ini otomatis mewarisi constructor (`__init__`) dari `Lampu`.

### 4. Polymorphism (Polimorfisme)
Method `nyala()` didefinisikan ulang (**override**) secara berbeda di setiap subclass (`LampuMerah`, `LampuKuning`, `LampuHijau`). Saat dipanggil dari objek yang berbeda, hasilnya pun berbeda meskipun nama method-nya sama:

```python
self.merah.nyala()   # "Lampu Yang Sedang Menyala Adalah Warna Merah"
self.kuning.nyala()  # "Lampu Yang Sedang Menyala Adalah Warna Kuning"
self.hijau.nyala()   # "Lampu Yang Sedang Menyala Adalah Warna Hijau"
```

### 5. Abstraction (Abstraksi)
Class `Lampu` dibuat sebagai **abstract class** menggunakan modul `abc`, dengan method `nyala()` sebagai **abstract method**:

```python
class Lampu(ABC):
    @abstractmethod
    def nyala(self):
        pass
```

Karena bersifat abstrak, class `Lampu` **tidak dapat langsung dibuat objeknya** (`Lampu("HIJAU")` akan menghasilkan error). `Lampu` hanya berfungsi sebagai kontrak/cetakan yang mewajibkan setiap subclass-nya (`LampuMerah`, `LampuKuning`, `LampuHijau`) mengimplementasikan method `nyala()` sendiri.

## Alur Program

1. Program dimulai dengan kondisi awal lampu **HIJAU**
2. Setiap 5 detik, `PrintColor()` dipanggil untuk:
   - Membersihkan layar terminal
   - Menampilkan tampilan lampu dengan warna aktif menyala terang dan warna lain redup
   - Berpindah ke warna berikutnya sesuai urutan lalu lintas standar
3. Proses berulang terus-menerus (infinite loop)

## Catatan

Dokumentasi ini dibuat sebagai pelengkap untuk memudahkan pemahaman terhadap source code `index.py`.