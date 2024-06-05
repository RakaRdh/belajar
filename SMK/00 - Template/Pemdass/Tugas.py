import datetime

nik=[]
nama=[]
alamat=[]
nohp=[]
asalsekolah=[]
ttgl=[]
jalur=[]

def show_menu():
    print('''========== MENU ==========
1) Tampilkan Data
2) Tambahkan Data
3) Rubah Data
4) Hapus Data
5) Pilih Jalur
6) Exit
========== MENU ==========''')

    pilihan=int(input('Masukan Pilihan Anda: '))
    if pilihan==1:
        show_data()
    elif pilihan==2:
        add_data()
    elif pilihan==3:
        change_data()
    elif pilihan==4:
        remove_data()
    elif pilihan==5:
        Jalur()
    elif pilihan==6:
        keluar()
    else:
        print('Pilihan anda tidak ada')
        show_menu()

def show_data():
    global nik
    global nama
    global alamat
    global nohp
    global asalsekolah
    global ttgl

    if len(nik) <= 0:
        print('------------------------------------')
        print('====== BELUM ADA DATA ======')
        print('------------------------------------')
        show_menu()
    
    if len(nik) >= 0:
        print('------------------------------------')
        print('NIK                  = ',nik)
        print('Nama                 = ',nama)
        print('Alamat               = ',alamat)
        print('No. HP               = ', nohp)
        print('Asal Sekolah         = ',asalsekolah)
        print('Tempat Tanggal lahir = ',ttgl)
        print('Jalur yang dipilih   = ',jalur)
        print('------------------------------------')
        show_menu()

def add_data():
    global nik
    global nama
    global alamat
    global nohp
    global asalsekolah
    global ttgl

    nik2 = input('NIK                 = ')
    nik.append(nik2)

    nama2 = input('Nama                 = ')
    nama.append(nama2)
        
    alamat2 = input('Alamat               = ')
    alamat.append(alamat2)

    nohp2 = input('No. HP               = ')
    nohp.append(nohp2)

    asalsekolah2 = input('Asal Sekolah         = ')
    asalsekolah.append(asalsekolah2)

    ttgl2 = input('Tempat Tanggal lahir = ')
    ttgl.append(ttgl2)

    print()
    show_menu()

def change_data():
    global nik
    global nama
    global alamat
    global nohp
    global asalsekolah
    global ttgl

    del nik[:]
    del nama[:]
    del alamat[:]
    del nohp[:]
    del asalsekolah[:]
    del ttgl[:]

    nik.append(str(input("NIK                    : ")))
    nama.append(str(input("Nama                   : ")))
    ttgl.append(str(input("Tempat Tanggal Lahir   : ")))
    alamat.append(str(input("Alamat                 : ")))
    nohp.append(str(input("NO HP                  : ")))
    asalsekolah.append(str(input("Asal Sekolah           : ")))

    show_menu()

def remove_data():
    global nik
    global nama
    global alamat
    global nohp
    global asalsekolah
    global ttgl

    hapus = input('Apakah Anda ingin menghapus data Anda ? (Y/T) : ')
    if hapus == 'y' or hapus == 'Y':
        del nik[:]
        del nama[:]
        del alamat[:]
        del nohp[:]
        del asalsekolah[:]
        del ttgl[:]

        print('------------------------------------')
        print('=== DATA ANDA SUDAH DIHAPUS ===')
        print('------------------------------------')
        show_menu()
    
    elif hapus == 't' or hapus == 'T':
        show_menu()
    
    else:
        print('------------------------------------')
        print('Pilihan Anda tidak ada')
        print('------------------------------------')
        remove_data()

def Jalur():
    global jalur
    global jalur1
    global jalur2
    global jalur3
    global jalur4

    print ('=== JALUR PENDAFTARAN ===')
    print('1. JPK       >>> GRATIS')
    print('2. PMDK      >>> Rp.350,000')
    print('3. Prestasi  >>> Rp.375,000')
    print('4. Mandiri   >>> Rp.400,000')
    print()

    ppdb = int(input('Masukkan Pilihan Jalur Anda :'))
    if ppdb == 1 :
        jalur1 = 'JPK'
        jalur.append(jalur1)
        show_menu()

    elif ppdb == 2 :
        jalur2 = 'PMDK'
        jalur.append(jalur2)
        show_menu()

    elif ppdb == 3 :
        jalur3 = 'PRESENTASI'
        jalur.append(jalur3)
        show_menu()

    elif ppdb == 4:
        jalur4 = 'MANDIRI'
        jalur.append(jalur4)
        show_menu()

    else :
        print('------------------------------------')
        print('Pilihan Tidak Tersedia, Tolong Pilih dengan Benar!')
        print('------------------------------------')
        Jalur()

def keluar():
    out = input('Apakah Anda ingin keluar ? (Y/T) : ')
    if out == 'y' or out == 'Y':
        print('------------------------------------')
        print('Terimakasih telah berkunjung !')
        print('Waktu = ',datetime.datetime.now())
        print('------------------------------------')
        exit()
    
    elif out == 't' or out == 'T':
        show_menu()

show_menu()