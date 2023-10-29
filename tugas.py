print('----Kendaraan----')
my_list = ['Ferrari 488 Pista', 'Mobil', 3.9, 'Merah', 4]
my_list.append (14.8)
my_list.append ('Sport')
my_list.insert (2, 'Ferrari')

print(my_list)

print('----Luas Bangun Datar----')

bangun_datar = int(input('Menghitung luas: '))

match bangun_datar:
    case 1:
         sisi = int(input('Masukan sisi: '))
         rumus_p = sisi*sisi
         print('Luas persegi adalah',(rumus_p))
    case 2:
        jari_jari = float(input('Masukan jari jari: '))
        rumus_l =3.14*jari_jari*jari_jari
        print('Luas lingkarang adalah', rumus_l)        
    case 3:
        alas = int(input('Masukan alas: '))
        tinggi = int(input('Masukan tinggi: '))
        rumus_segitiga = alas*tinggi/2
        print('Luas segitiga adalah', (alas,tinggi))

          



