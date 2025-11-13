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
        
        tugas_lama = database.list_tugas[indeks]["judul"]
        
        print(f"Mengubah tugas {tugas_lama}")
        
        tugas_baru = input("Masukan judul baru : ")
        nama_baru = input("Masukan nama baru : ")
        desc_baru = input("Masukan desc baru : ")
        
        if tugas_baru:
            database.list_tugas[indeks]["judul"] = tugas_baru
        if nama_baru:
            database.list_tugas[indeks]["diberikan"] = nama_baru
        if desc_baru:
            database.list_tugas[indeks]["desc"] = desc_baru
            
        read() 
    except ValueError:
        print(f"input harus berupa angka")