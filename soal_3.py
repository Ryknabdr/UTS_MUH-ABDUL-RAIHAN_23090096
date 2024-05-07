def hitung_total(harga_barang):
    total_harga = sum(harga_barang)
    return total_harga

print("selamat datang di kantin poltek")
jumlah_barang = int(input(" silahkan Masukkan jumlah barang: "))

harga_barang = []
for i in range(jumlah_barang):
    harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
    harga_barang.append(harga)

total_harga = hitung_total(harga_barang)

print(f"Total belanjaan jadi: Rp {total_harga}")
print("terima kasih telah berbelanja di kantin kami2")