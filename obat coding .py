print("======= DATA OBAT APOTEK =======")
obat = {
    1: {"nama": "Paracetamol", "harga": 25000, "stok": 20},
    2: {"nama": "Amoxicillin", "harga": 30000, "stok": 15},
    3: {"nama": "Antasida", "harga": 20000, "stok": 25},
    4: {"nama": "Ibuprofen", "harga": 35000, "stok": 10},
    5: {"nama": "CTM", "harga": 40000, "stok": 12},
    6: {"nama": "Vitamin C", "harga": 43000, "stok": 30},
    7: {"nama": "OBH", "harga": 50000, "stok": 18},
    8: {"nama": "Oralit", "harga": 55000, "stok": 0},
    9: {"nama": "Cetirizine", "harga": 40000, "stok": 14},
    10: {"nama": "Antiseptik", "harga": 70000, "stok": 8}
}
for nomor, data in obat.items():
    print(nomor, ".", data["nama"])
pilihan = int(input("\nPilih nomor obat: "))
if pilihan in obat:
    data = obat[pilihan]
    nama = data["nama"]
    harga = data["harga"]
    stok = data["stok"]
    status = "Stok tersedia" if stok > 0 else "Stok habis"
    print("\n======= DETAIL OBAT ========")
    print("Nomor obat:", pilihan)
    print("Nama obat:", nama)
    print("Harga obat: Rp", format(harga, ",").replace(",", "."))
    print("Jumlah stok:", stok)
    print("Status:", status)
else:
    print("Pilihan obat tidak valid")
