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
        
        judul_lama = database.list_tugas[indeks][0]
        
        print(f"Mengubah tugas {judul_lama}")
        
        judul_baru = input("Masukan judul baru")
        nama_baru = input("Masukan nama baru")
        desc_baru = input("Masukan desc baru")
        
        if judul_baru:
            database.list_tugas[indeks][0] = judul_baru
        if nama_baru:
            database.list_tugas[indeks][0] = nama_baru
        if desc_baru:
            database.list_tugas[indeks][0] = desc_baru
            
        read() 
    except ValueError:
        print(f"input harus berupa angka")