def prodi(prodi): 

    print(f"Saya sedang belajar di program studi {prodi}.") 

 

def total_siswa(SNBP, SNBT): 

    total = SNBP + SNBT 

    return total 

 

total = total_siswa(100, 150) 

prodi("Teknik Komputer") 

print(f"Total siswa: {total}\n") 

 

class KEL13: 

    def __init__(self, nama, nim, IPK): 

        self.nama = nama 

        self.nim = nim 

        self.IPK = IPK 

 

    def cek_IPK(self): 

        if self.IPK >= 3.5: 

            return "Status: Cum Laude" 

        else: 

            return "Status: Tidak Cum Laude" 

 

daftar_mahasiswa = [ 

    KEL13("FELIM A", "111", 3.7), 

    KEL13("RAFAEL WIDYUTA A", "066", 3.2), 

    KEL13("GHULAM ABIYYU GAMASETYA", "088", 3.9), 

    KEL13("ALDERIL BAGUS OKTADO AZIZ", "123", 3.3), 

    ] 

 

daftar_ipk = [] 

 

for mahasiswa in daftar_mahasiswa: 

        print(f"Halo! Saya {mahasiswa.nama}, dengan NIM {mahasiswa.nim}.") 

        status_ipk = mahasiswa.cek_IPK() 

        print(status_ipk) 

        print("-" * 30) 

        daftar_ipk.append(mahasiswa.IPK) 

 

print("berikut daftar IPK mahasiswa:") 

print(daftar_ipk) 