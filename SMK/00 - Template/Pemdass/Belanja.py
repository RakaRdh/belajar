def belanja():
    harga = int(input('Masukkan harga :'))

    if harga > 1000000:
        print('Anda mendapatkan diskon 10%')
        print('Total yang harus anda bayar adalah Rp.', float(harga - harga * 0.1))

    else:
        print('Anda tidak mendapatkan diskon!')
        print('Total yang harus anda bayar adalah Rp.', float(harga))

belanja()