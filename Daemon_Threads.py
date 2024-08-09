# Daemon Thread
# Thread yang berjalan di background karena tidak penting untuk program
# Thread akan terus berjalan sampai program ditutup
import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print()
        print("Berjalan", count, "detik")
        
x = threading.Thread(target=timer, daemon=True)
x.start()

# print(x.isDaemon())

user = input("Ketik untuk keluar: ")