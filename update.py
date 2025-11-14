import database
from read import read 

def update():
    print(f"=== Update ===")
    
    if not read():
        return
    
    try:
        nomor = int(input("Masukan nomor yang diubah : "))
        if nomor < 1 or nomor > len(database.list_tugas):
            print(f"Masukan angka yang benar")
            return 
        
        indeks = nomor - 1
        
        tugas_lama = database.list_tugas[indeks]
        
        print(f"Mengubah tugas {tugas_lama}")
        
        judul_baru = input("Masukan judul baru : ")
        nama_baru = input("Masukan nama baru : ")
        deskripsi_baru = input("Masukan Deskripsi baru : ")
        
        tugas_lama.ubah_data(judul_baru, nama_baru, deskripsi_baru)
            
        read() 
    except ValueError:
        print(f"input harus berupa angka")