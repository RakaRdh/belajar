nik=[]
nama=[]
alamat=[]
nohp=[]
asalsekolah=[]
ttgl=[]
jalur=[]

def show_data():
    global nik
    global nama
    global ttgl
    global alamat
    global nohp
    global asalsekolah  
    if len(nik) <= 0:
        print("BELUM ADA DATA")
        show_menu()
    elif len(nik) >=0:
        print ("NIK                  :",nik)
        print ("Nama                 :",nama)
        print ("Tempat Tanggal Lahir :",ttgl)
        print ("Alamat               :",alamat)
        print ("NO HP                :",nohp)
        print ("Asal Sekolah         :",asalsekolah)
        print ("Jalur                :",jalur)
        show_menu()

def add_data():
    global nik
    global nama
    global ttgl
    global alamat
    global nohp
    global asalsekolah    
    nik2 = input("NIK                    : ")
    nik.append(nik2)

    nama2 = input("Nama                   : ")
    nama.append(nama2)
    
    ttgl2 = input("Tempat Tanggal Lahir   : ")
    ttgl.append(ttgl2)
    
    alamat2 = input("Alamat                 : ")
    alamat.append(alamat2)
    
    nohp2 = input("NO HP                  : ")
    nohp.append(nohp2)

    asalsekolah2 = input("Asal Sekolah           : ")
    asalsekolah.append(asalsekolah2)
    show_menu()

def change_data():
    global nik
    global nama
    global ttgl
    global alamat
    global nohp
    global asalsekolah 

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
    global ttgl
    global alamat
    global nohp
    global asalsekolah 
    print('Apakah anda ingin menghapus data?')
    pilihan=input("masukan pilihan y/t: ")
    if pilihan=="y":

        del nik[:]
        del nama[:]
        del alamat[:]
        del nohp[:]
        del asalsekolah[:]
        del ttgl[:]
    
        print("data anda sudah terhapus")
        show_menu()
    elif pilihan=="t":
        show_menu()
    else:
        print("pilihan anda tidak ada")
        remove_data()
    
def exit():
    print("Terima Kasih telah berkunjung!")
    exit()

def Jalur():   
        global jalur1
        global jalur2
        global jalur3
        global jalur4
        global jalur
        print ("JALUR PENDAFTARAN")
        print("1. JPK       >>> GRATIS")
        print("2. PMDK      >>> Rp.350,000")
        print("3. Prestasi  >>> Rp.375,000")
        print("4. Mandiri   >>> Rp.400,000")
        ppdb = int(input("Masukkan Pilihan Jalur Anda :"))
        if ppdb == 1 :
            jalur1 = "JPK"
            jalur.append(jalur1)
            show_menu()
        elif ppdb == 2 :
            jalur2 = "PMDK"
            jalur.append(jalur2)
            show_menu()
        elif ppdb == 3 :
            jalur3 = "PRESENTASI"
            jalur.append(jalur3)
            show_menu()
        elif ppdb == 4:
            jalur4 = "MANDIRI"
            jalur.append(jalur4)
            show_menu()
        else :
            print("Pilihan Tidak Tersedia, Pilih Ynag Benar !!")
            Jalur()
    


def show_menu():
    print()
    print("----------- MENU ----------")
    print("1) Tampilkan data")
    print("2) tambahkan data")
    print("3) Rubah data")
    print("4) Hapus data")
    print("5) Pilih jalur")
    print("6) Exit")
    print()

    pilihan=int(input("masukan pilihan anda:"))
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
        print("Terima kasih telah berkunjung!")
        exit()
    else:
        print("Pilihan anda tidak ada")
        show_menu()

show_menu()