opsi = int(input("=============================\n"
"Selamat datang di kalkulator Anveg Balwana!\n"
"Silahkan pilih Opsi :\n"
"1. Dominasi\n"
"2. Frekuensi\n"
"3.Densitas\n"
"=============================\n"
"Opsi yang dipilih :"))

if opsi == 1:
    kanopi = float(input("Masukkan nilai persentase tutupan tajuk: "))
    luas_petak = float(input("Masukkan nilai total luas petak :"))
    dominasi_mutlak_i = kanopi/luas_petak*1
    total_dominasi_mutlak_vegetasi = float(input("Masukkan nilai total dominasi mutlak seluruh jenis :"))
    dominasi_relatif = dominasi_mutlak_i/total_dominasi_mutlak_vegetasi*1
    print("Dominasi mutlak jenis i adalah : ", f"{dominasi_mutlak_i:,.2%}")
    print("Dominasi Relatif jenis i adalah : ", f"{dominasi_relatif:,.2%}")
