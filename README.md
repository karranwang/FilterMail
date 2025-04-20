# Email Filter & Formatter

![Preview](images.jpg)

**Email Filter & Formatter** adalah tool berbasis Python untuk memproses dan merapikan daftar email dari file teks. Tool ini dirancang untuk memfilter email valid, menghapus duplikat, dan menyimpan hasilnya dalam format yang rapi dan terstruktur.

## Fitur

- Validasi email otomatis
- Menghapus karakter pemisah seperti: `,`, `:`, `|`, spasi, tab
- Menghapus email duplikat
- Opsi output:
  - Gabung semua email ke satu file (`sorted_email.txt`)
  - Pisah berdasarkan huruf awal ke file terpisah (`A.txt`, `B.txt`, dst)
- Output disimpan otomatis ke folder `output/`
- Tampilan CLI yang bersih dan interaktif

## Cara Penggunaan

1. Pastikan kamu memiliki Python 3.x terinstal.
2. Jalankan script:

```bash
python main.py

output/
├── sorted_email.txt         # Jika memilih mode gabung
├── A.txt, B.txt, ...        # Jika memilih mode per huruf
