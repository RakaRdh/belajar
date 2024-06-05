def belanja():
    harga = int(input('Masukkan total harga belanja Anda : '))

    if harga >= 500000 and harga < 1000000:
        total1 = harga - (harga * 0.1)
        print('Anda mendapatkan diskon sebesar 10%')
        print('Total yang harus Anda bayar adalah Rp.', float(total1))

    elif harga >= 1000000 and harga < 2000000:
        total2 = harga - (harga * 0.2)
        print('Anda mendapatkan diskon sebesar 20%')
        print('Total yang harus Anda bayar adalah Rp.', float(total2))
    
    elif harga >= 2000000:
        total3 = harga - (harga * 0.3)
        print('Anda mendapatkan diskon sebesar 30%')
        print('Total yang harus Anda bayar adalah ', total3)
    
    else:
        print('Anda tidak mendapatkan diskon. Total yang harus dibayar adalah ', harga)
    

belanja()