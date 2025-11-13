import database
from read import read

def create():
    print("=== Tambah Tugas ===")
    judul_tugas = input("Masukan Judul Tugas : ")
    deskripsi_tugas = input("Masukan Deskripsi : ")
    diberikan_kepada = input("Masukan Nama : ")
    tugas = [judul_tugas, diberikan_kepada, deskripsi_tugas]
    
    database.list_tugas.append(tugas)
    read()
