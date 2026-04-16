l = [
    ["Asus Vivobook", 7000000, 3],
    ["Acer Aspire", 6500000, 2],
    ["Lenovo IdeaPad", 8000000, 5]
]

while True:
    print("\n=== TOKO LAPTOP ===")
    print("1. Lihat Laptop")
    print("2. Beli Laptop")
    print("3. Keluar")

    x = input("Pilih menu: ")

    if x == "1":
        for i in range(len(l)):
            print(str(i+1) + ". " + l[i][0] + " - Rp" + str(l[i][1]) + " - Stok: " + str(l[i][2]))

    elif x == "2":
        for i in range(len(l)):
            print(str(i+1) + ". " + l[i][0])

        a = int(input("Pilih laptop: ")) - 1
        b = int(input("Jumlah beli: "))

        # proses beli laptop
        if a >= 0 and a < len(l):
            if l[a][2] >= b:
                total = l[a][1] * b
                l[a][2] = l[a][2] - b
                print("Berhasil beli")
                print("Total bayar = Rp" + str(total))
            else:
                print("stok tidak cukup")
        else:
            print("pilihan salah")

    elif x == "3":
        print("terima kasih")
        break

    else:
        print("menu salah")