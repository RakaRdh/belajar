import random
import datetime
from customer import Customer

cust = Customer(id)

#Pin = 1234
while True:
    id = int(input('Masukkan pin anda :'))
    trial = 0

    while (id != int(cust.checkPin()) and trial < 3):
        id = int(input('Pin Anda salah. Masukkan pin lagi :'))

        trial += 1
        
        if trial == 3:
            print('Error, silahkan ambil kartu dan coba lagi..')
            exit()
        
    while True:
        if id == int(cust.checkPin()):
            print('Selamat Datang di ATM Ceriaa')
            print('''
== Pilihan Menu ==
1) Cek saldo
2) Debet
3) Simpan
4) Ganti pin
5) Keluar 
            ''')

        pilihan = int(input('Silahkan pilih menu :'))
        if pilihan == 1:
            print('================================')
            print('Saldo Anda ada '+ str(cust.checkBalance()))
            print('================================')

        elif pilihan == 2:
            print('================================')
            nominal = int(input('Masukkan jumlah uang yang ingin ditarik : '))
            cust.withdrawBalance(nominal)

                     
            if nominal <= cust.checkBalance():
                print('Uang Anda sisa : ' + str(cust.checkBalance()))
                print('================================')

            elif nominal > cust.checkBalance():
                print('Anda tidak bisa menarik uang sebanyak itu!')
                print('================================')
                    
            else:
                print('Keyword Anda salah!')
                print('================================')
        
        elif pilihan == 3:
            print('================================')
            nominal = int(input('Masukkan jumlah uang yang ingin ditambahkan : '))
            cust.depositBalance(nominal)
           
            print('Uang Anda bertambah menjadi :' + str(cust.checkBalance()))
            print('================================')


        elif pilihan == 4:
            print('================================')
            PinLama = int(input('Masukkan Pin lama Anda :'))
            trial = 0

            while (PinLama != int(cust.checkPin()) and trial < 3):
                PinLama = int(input('Pin lama Anda salah. Masukkan pin lagi :'))

                trial += 1
        
                if trial == 3:
                    print('Pin yang Anda masukkan salah!')
                    print('================================')
                    exit()

            while True:
                if PinLama == int(cust.checkPin()):                    
                    print('Silahkan lanjutkan ketahap berikutnya. ')

                    PinBaru = int(input('Masukkan Pin baru : '))
                    verifikasiPin = int(input('Masukkan kembali Pin baru Anda : '))

                    if PinBaru == verifikasiPin:
                        print('Pin Anda berhasil diubah. ')
                        print('================================')
                        break

                    else:
                        print('Pin Anda salah!')
                        print('================================')
        
        elif pilihan == 5:
            
            print('============ RECORD ============')
            print('Berikut nomor resi Anda : ' + str(random.randint(100000, 1000000)))
            print('Tanggal/waktu saat ini  : ' + str(datetime.datetime.now()))
            print('Saldo Anda sekarang adalah : ' + str(cust.checkBalance()))
            print('Terimakasih telah datang ke ATM Ceriaa :)')
            print('============ RECORD ============')
            print('')
            exit()
        
        else:
            print('================================')
            print('Keyword Anda salah!')
            print('================================')