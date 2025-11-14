import database
from read import read
from tugas import Tugas

def create():
    print("=== Tambah Tugas ===")
    judul_tugas = input("Masukan Judul Tugas : ")
    deskripsi_tugas = input("Masukan Deskripsi : ")
    diberikan_kepada = input("Masukan Nama : ")
    
    tugas_baru = Tugas(judul = judul_tugas, nama = diberikan_kepada, deksripsi=deskripsi_tugas)
    
    database.list_tugas.append(tugas_baru)
    read()
