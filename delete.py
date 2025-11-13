import database
from read import read

def delete():
    print(f"=== Delete ===")
    
    if not read:
        return
    
    try:
        nomor = int(input("Masukan angka yang ingin di hapus"))
        
        if nomor < 1 or nomor > len(database.list_tugas):
            print(f"Masukan nomor yang benar")
            return
        
        indeks = nomor - 1
        
        tugas_hapus = database.list_tugas[indeks]
        konfirmasi = input(f"{tugas_hapus[0]} Hapus? | Masukan y/n")
        
        if konfirmasi == 'y':
            database.list_tugas.pop(indeks)
        else:
            print(f"Gagal menghapus")
            
        read()
        
    except ValueError:
        print("Input berupa angka")
            