
def create():
    list_tugas = []
    while True:
        judul_tugas = input("Masukan Judul Tugas : ")
        deskripsi_tugas = input("Masukan Deskripsi : ")
        diberikan_kepada = input("Masukan Nama : ")
        tugas = [judul_tugas, diberikan_kepada, deskripsi_tugas]
        list_tugas.append(tugas)
        
        print(f"No\t | Judul\t | Nama\t\t | Deskripsi\t\t ")
        for no,item in enumerate (list_tugas):
            judul = item[0]
            nama = item[1]
            desc = item[2]
            print(f"{no+1}     \t{judul}   \t{nama}  \t\t {desc}")
            
        lanjut = input("Lanjut memasukan tugas (y/n)")   
        if lanjut.lower() == 'n':
            break 
    print("selesai")
create()