import database

def read():
    print(f"\n --- Read Tugas ---")
    
    if not database.list_tugas:
        print(f"Daftar tugas masih kosong")
        return False
    
    print(f"No\t | Tugas\t | Nama\t | Deskripsi\t")
    print("="*40)
    
    for no, item in enumerate (database.list_tugas):
        judul = item[0]
        nama = item[1]
        desc = item[2]
        print(f"{no+1}\t {judul}\t {nama}\t {desc}\t")
        
    return True 