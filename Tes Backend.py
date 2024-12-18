def hitung_gaji(jam_kerja, tarif_per_jam):
    # Konstanta jumlah jam kerja normal dalam seminggu
    jam_normal = 40
    tarif_lembur = 1.5 * tarif_per_jam

    if jam_kerja <= jam_normal:
        gaji = jam_kerja * tarif_per_jam
    else:
        jam_lembur = jam_kerja - jam_normal
        gaji = (jam_normal * tarif_per_jam) + (jam_lembur * tarif_lembur)

    return gaji

# Input jumlah jam kerja dan tarif per jam
try:
    jam_kerja = float(input("Masukkan jumlah jam kerja: "))
    tarif_per_jam = float(input("Masukkan tarif per jam: "))

    # Hitung gaji
    gaji = hitung_gaji(jam_kerja, tarif_per_jam)

    # Tampilkan hasil
    print(f"Gaji total: Rp {gaji:.2f}")

except ValueError:
    print("Input tidak valid. Pastikan Anda memasukkan angka.")