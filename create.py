import database
from read import read

def create():
    print("=== Tambah Tugas ===")
    judul_tugas = input("Masukan Judul Tugas : ")
    deskripsi_tugas = input("Masukan Deskripsi : ")
    diberikan_kepada = input("Masukan Nama : ")
    tugas = {
        "judul": judul_tugas,
        "desc": deskripsi_tugas,
        "diberikan": diberikan_kepada
    }
    
    database.list_tugas.append(tugas)
    read()
