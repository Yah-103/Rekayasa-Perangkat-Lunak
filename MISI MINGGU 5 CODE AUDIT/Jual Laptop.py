daftar_laptop = [
    {
        "nama": "Asus Vivobook",
        "harga": 7000000,
        "stok": 3
    },
    {
        "nama": "Acer Aspire",
        "harga": 6500000,
        "stok": 2
    },
    {
        "nama": "Lenovo IdeaPad",
        "harga": 8000000,
        "stok": 5
    }
]


def tampilkan_menu():
    print("=== TOKO LAPTOP ===")
    print("1. Lihat Laptop")
    print("2. Beli Laptop")
    print("3. Keluar")


def tampilkan_laptop():
    print("Daftar Laptop:")

    for nomor, laptop in enumerate(daftar_laptop, start=1):
        print(
            f"{nomor}. {laptop['nama']} | "
            f"Harga: Rp{laptop['harga']} | "
            f"Stok: {laptop['stok']}"
        )


def beli_laptop():
    tampilkan_laptop()

    try:
        pilihan_laptop = int(input("Pilih laptop: ")) - 1
        jumlah_beli = int(input("Jumlah beli: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if pilihan_laptop < 0 or pilihan_laptop >= len(daftar_laptop):
        print("Pilihan laptop tidak valid.")
        return

    laptop_terpilih = daftar_laptop[pilihan_laptop]

    if jumlah_beli <= 0:
        print("Jumlah beli harus lebih dari 0.")
        return

    if jumlah_beli > laptop_terpilih["stok"]:
        print("Stok tidak mencukupi.")
        return

    total_harga = laptop_terpilih["harga"] * jumlah_beli
    laptop_terpilih["stok"] -= jumlah_beli

    print("Pembelian berhasil!")
    print(f"Laptop : {laptop_terpilih['nama']}")
    print(f"Jumlah : {jumlah_beli}")
    print(f"Total  : Rp{total_harga}")



def program_utama():
    while True:
        tampilkan_menu()
        pilihan_menu = input("Pilih menu: ")

        if pilihan_menu == "1":
            tampilkan_laptop()

        elif pilihan_menu == "2":
            beli_laptop()

        elif pilihan_menu == "3":
            print("Terima kasih telah menggunakan aplikasi.")
            break

        else:
            print("Menu tidak tersedia.")


program_utama()