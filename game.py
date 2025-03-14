import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    jumlah_tebakan = 0

    print("Selamat datang di game Tebak Angka!")
    print("Saya telah memilih angka antara 1 dan 100. Coba tebak!")

    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlah_tebakan += 1

            if tebakan < angka_rahasia:
                print("Tebakan Anda terlalu rendah. Coba lagi!")
            elif tebakan > angka_rahasia:
                print("Tebakan Anda terlalu tinggi. Coba lagi!")
            else:
                print(f"Selamat! Anda telah menebak angka {angka_rahasia} dengan {jumlah_tebakan} tebakan.")
        except ValueError:
            print("Tolong masukkan angka yang valid.")

if __name__ == "__main__":
    tebak_angka()