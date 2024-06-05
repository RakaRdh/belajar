def paketa():
    for i in range(20):
        if i % 2 == 0:
            print(i)
    menu()

def paketb():
    nilai = int(input('Masukkan Nilai Anda : '))

    if nilai >= 76 or nilai == 100:
        print('Anda Lulus !')
        menu()
    
    elif nilai <= 75:
        print('Anda Tidak Lulus !')
        menu()
    
    else:
        print('Masukkan nilai dari 1 - 100 !')
        menu()

def paketc():
    i = 1

    while i < 10:
        print(i)
        i += 2
    
    menu()

def paketd():
    harga = int(input('Masukkan total belanja : '))
    total_diskon = harga - (harga * 0.1)

    if harga > 1000000:
        print('Anda mendapatkan diskon sebesar 10 %')
        print('Total harga yang harus anda bayar adalah Rp.', str(total_diskon))
        menu()
    
    else:
        print('Anda tidak mendapatkan diskon !')
        print('Total harga yang harus Anda bayar adalah Rp.', str(harga))
        menu()

def menu():
    print('''
====================================
Paket UPRAK apa yang anda ingin jalankan ?
1. Perulangan genap ( For )
2. Nilai
3. Perulangan ganjil ( while )
4. Total belanja
====================================''')
    
    pilih = int(input('Masukkan nomor : '))
    
    if pilih == 1:
        paketa()
    
    elif pilih == 2:
        paketb()
    
    elif pilih == 3:
        paketc()
    
    elif pilih == 4:
        paketd()
    
    else:
        print('Tidak ada nomor yang anda masukkan')
    
menu()