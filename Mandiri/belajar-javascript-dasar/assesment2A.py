kodeVendor = input('Masukan Kode Vendor: ')
kodeBarang = input('Masukan Kode Barang: ')
namaBarang = input('Masukan Nama Barang: ')
total = int(input('Masukan Jumlah Box: '))
print("---------------------------------------")
i=0
countLolos=0
countTidakLolos=0
        
for i in range(total):
    berat = int(input("Masukan berat box ke-"+str(i+1)+":"))
    if(berat >=15 and berat <=17):
        countLolos=+1,
    elif(berat <15 and berat >17):
        print('Berat box tidak sesuai spesifikasi')
        countTidakLolos+=1   
    i=+1
persenLolos = countLolos/total*100,
persenTidakLolos = countTidakLolos/total*100,
print("---------------------------------------")
print("Persen tidak lolos= "+str(persenTidakLolos)+'%')
print("Persen lolos=" +str(persenLolos)+'%')
