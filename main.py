import os
import re

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_logo():
    print(r"""
 /$$   /$$           /$$$$$$$  /$$$$$$$            /$$   /$$
| $$  /$$/          | $$__  $$| $$__  $$          | $$$ | $$
| $$ /$$/   /$$$$$$ | $$  \ $$| $$  \ $$  /$$$$$$ | $$$$| $$
| $$$$$/   |____  $$| $$$$$$$/| $$$$$$$/ |____  $$| $$ $$ $$
| $$  $$    /$$$$$$$| $$__  $$| $$__  $$  /$$$$$$$| $$  $$$$
| $$\  $$  /$$__  $$| $$  \ $$| $$  \ $$ /$$__  $$| $$\  $$$
| $$ \  $$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$$| $$ \  $$
|__/  \__/ \_______/|__/  |__/|__/  |__/ \_______/|__/  \__/
   Email Filter & Formater by Karran - Github @karranwang
    """)

def is_valid_email(email):
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email.strip())

def sanitize_line(line):
    parts = re.split(r"[ \t|:;,]+", line)
    return [part.strip() for part in parts if is_valid_email(part.strip())]

def filter_emails(filename):
    if not os.path.isfile(filename):
        print(f"File '{filename}' tidak ditemukan.")
        return []

    valid_emails = []
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            valid_emails.extend(sanitize_line(line))

    return list(dict.fromkeys(valid_emails))  # Remove duplicates

def save_emails(emails, mode='gabung'):
    os.makedirs("output", exist_ok=True)

    if mode == 'gabung':
        with open("output/sorted_email.txt", "w", encoding='utf-8') as f:
            for email in sorted(emails):
                f.write(email + "\n")
        print("\n[+] Disimpan di: output/sorted_email.txt")

    elif mode == 'perhuruf':
        grouped = {}
        for email in emails:
            first = email[0].upper()
            grouped.setdefault(first, []).append(email)

        for huruf, daftar in grouped.items():
            with open(f"output/{huruf}.txt", "w", encoding='utf-8') as f:
                for email in sorted(daftar):
                    f.write(email + "\n")
        print("\n[+] Disimpan di folder: output/ sebagai A.txt, B.txt, ...")

def main():
    clear_screen()
    print_logo()
    filename = input("Masukkan nama file email (misal: mailist.txt): ").strip()

    print("\nMode output:")
    print("1. Gabung semua ke 1 file (sorted_email.txt)")
    print("2. Pisah per huruf awal (A.txt, B.txt, dst)")

    mode = input("Pilih mode [1/2]: ").strip()
    mode = 'gabung' if mode == '1' else 'perhuruf'

    print("\n[~] Memproses...")
    emails = filter_emails(filename)

    if emails:
        save_emails(emails, mode)
    else:
        print("[!] Tidak ada email valid ditemukan.")

if __name__ == "__main__":
    main()
