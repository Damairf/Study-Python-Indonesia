# Threading
# Mengatur urutan yang akan dijalankan oleh komputer
import threading
import time

def sarapan():
    time.sleep(3)
    print("Kamu selesai sarapan")
    print()
    
def olahraga():
    time.sleep(4)
    print("Kamu selesai olahraga")
    print()
    
def belajar():
    time.sleep(5)
    print("Kamu selesai belajar")
    print()
  
x  = threading.Thread(target=sarapan, args=())      # Akan menampilkan berapa urutan yang akan dikerjakan
x.start()                                           # Dalam contoh akan menampilkan 4 urutan
y = threading.Thread(target=olahraga, args=())      # Karena untuk 3 def pertama masih belum dikerjakan
y.start()
z = threading.Thread(target=belajar, args=())
z.start()

x.join()        # Akan menjalankan perintah terlebih dahulu sehingga hanya akan menampilkan 1 thread
y.join()        # Masih tersisa 1 karena masih terdapat perintah print dibawah
z.join()

# sarapan()
# olahraga()    
# belajar()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())