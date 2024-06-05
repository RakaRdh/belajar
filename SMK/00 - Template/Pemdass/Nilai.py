def ulangan():
    nilai = int(input('Masukkan nilai Anda : '))

    if nilai >= 76 :
        print('Anda lulus')
    
    elif nilai <= 75 or nilai == 50:
        print('Anda remed')
    
    else:
        print('Anda tidak lulus')

ulangan()