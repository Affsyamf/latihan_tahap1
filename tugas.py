class Tugas:
    def __init__(self, judul, nama, deksripsi):
        self.judul = judul
        self.nama = nama
        self.deskripsi = deksripsi
        self.status = "Belum Selesai"
        
    def tandai_selesai(self):
        self.status = "Sudah Selesai"
        print(f"Tugas '{self.judul}' telah ditandai selesai")
        
    def ubah_data(self, judul_baru, nama_baru, deskripsi_baru):
        if judul_baru:
            self.judul = judul_baru
        if nama_baru:
            self.nama = nama_baru
        if deskripsi_baru:
            self.deskripsi = deskripsi_baru
            