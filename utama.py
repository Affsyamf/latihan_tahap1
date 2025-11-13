from create import create
from read import read
from delete import delete
from update import update
from header import header

def utama():
    while True:
        header()
        print("\n" + "="*20 + "Utama" + "="*20)
        print("1. tambah tugas")
        print("2. lihat tugas")
        print("3. edit tugas")
        print("4. delete tugas")
        print("5. keluar")
        
        pilih = int(input("Masukan Pilihan (1-5) : "))
        
        if pilih == '1':
            create()
        elif pilih == '2':
            read()
        elif pilih == '3':
            update()
        elif pilih == '4':
            delete()
        elif pilih == '5':
            break
        else: 
            print("Pilihan tidak valid")
            
if __name__ == "__main__":
    utama()
        
        