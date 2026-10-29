# UTS_PBO — Pipeline Data Karyawan dan Sensor

Project Python sederhana menggunakan OOP, inheritance, abstract method, dan polymorphism. Project membaca dua file JSON lalu menghasilkan laporan CSV.

## Struktur folder

```text
UTS_PBO/
├── data/
│   ├── employee.json
│   └── sensor_logs.json
├── output/
│   ├── employee_report.csv   (dibuat saat program dijalankan)
│   └── sensor_report.csv     (dibuat saat program dijalankan)
├── processors/
│   ├── __init__.py
│   ├── base_processor.py
│   ├── employee_processor.py
│   └── sensor_processor.py
├── runners/
│   ├── __init__.py
│   └── runner_pipeline.py
├── main.py
└── README.md
```

## Cara menjalankan di Visual Studio Code (Windows)

1. Ekstrak `UTS_PBO.zip` ke folder yang mudah ditemukan.
2. Buka VS Code.
3. Pilih **File → Open Folder...**, lalu pilih folder `UTS_PBO` (folder yang berisi `main.py`).
4. Pastikan Python sudah terpasang. Buka terminal VS Code melalui **Terminal → New Terminal**.
5. Periksa Python:
   ```powershell
   python --version
   ```
   Jika perintah itu tidak tersedia, coba:
   ```powershell
   py --version
   ```
6. Jika Python tersedia, jalankan dari folder utama `UTS_PBO`:
   ```powershell
   python main.py
   ```
   Jika perintah `python` tidak tersedia, gunakan:
   ```powershell
   py main.py
   ```
7. Setelah selesai, buka folder `output`. File `employee_report.csv` dan `sensor_report.csv` akan dibuat otomatis.
8. Klik file CSV untuk melihat hasilnya di VS Code. File CSV juga bisa dibuka dengan Microsoft Excel.

## Menjalankan file runner secara langsung

Dari folder utama project, jalankan:

```powershell
python -m runners.runner_pipeline
```

## Catatan

- Jalankan perintah dari folder utama project, bukan dari dalam folder `processors` atau `runners`.
- Library yang digunakan semuanya bawaan Python; tidak perlu `pip install`.
- `operator_id: null` di JSON adalah data kosong yang valid dan akan menjadi kolom kosong di CSV.
- Data sensor mengikuti 30 baris pada gambar referensi.
