# MultiProcessing
# Menjalankan perintah di paralel dalam core cpu yang berbeda
# Multiprocessing = Lebih baik digunakan untuk tugas cpu yang terikat (pemakaian berat cpu)
# Multithreading = Lebih baik digunakan untuk tugas io yang terikat
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1
        
def main():
    print(cpu_count())      # Mencetak komputer kita memiliki berapa cpu (Sebagai patokan untuk menjalankan suatu perintah)
    
    # Menghitung 1M detik lebih baik dipisah berdasarkan kekuatas cpu, seperti misal pc ini memiliki
    # 16 thread cpu, sehingga lebih baik tugas dibagi menjadi beberapa bagian (penting tidak melebihi cpu)
    # Seperti kasus menghitung 1M jika hanya dijalankan oleh 1 tugas maka akan selesai hampir 1 menit
    # Tetapi jika dibagi menjadi 10 seperti dibawah ini, maka akan selesai dalam waktu 17 detik
    a = Process(target=counter, args=(100000000,))
    b = Process(target=counter, args=(100000000,))
    c = Process(target=counter, args=(100000000,))
    d = Process(target=counter, args=(100000000,))
    e = Process(target=counter, args=(100000000,))
    f = Process(target=counter, args=(100000000,))
    g = Process(target=counter, args=(100000000,))
    h = Process(target=counter, args=(100000000,))
    i = Process(target=counter, args=(100000000,))
    j = Process(target=counter, args=(100000000,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    
    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    
    print("Berhitung selesai dalam", time.perf_counter(), "detik")

if __name__ == '__main__':
    main()