import database

def read():
    print(f"\n --- Read Tugas ---")
    
    if not database.list_tugas:
        print(f"Daftar tugas masih kosong")
        return False
    
    print(f"No\t | Tugas\t | Nama\t | Deskripsi\t")
    print("="*40)
    
    for no, item in enumerate (database.list_tugas):
        print(f"{no+1}\t {item.judul}\t {item.nama}\t {item.deskripsi} ({item.status}) \t")
        
    return True 