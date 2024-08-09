# Time Module
import time

print(time.ctime(0))        # Menampilkan waktu epoch pada komputer
print()                     # epoch = Ketika komputer berpikir waktu pertama yang tertanam (reference point)

print(time.time())          # Menampilkan jarak berapa detik waktu saat ini dengan waktu epoch
print()

print(time.ctime(time.time()))      # Menampilkan waktu saat ini
print()

time_object = time.localtime()      # Menampilkan waktu saat ini dengan detail tapi format sulit dibaca
print(time_object)
print()

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)           # Membuat format localtime menjadi lebih mudah dibaca
print()

time_gm = time.gmtime()     # Menampilkan waktu UTC / format global
print(time_gm)
print()

time_string = "29 July, 2024"
time_obj = time.strptime(time_string, "%d %B, %Y")
print(time_obj)             # Menampilkan waktu tetapi hanya dengan beberapa perintah
print()

# (Tahun, Bulan, Tanggal, Jam, Menit, Detik, Hari dalam seminggu, Bulan dalam setahun, dst)
time_tuple = (2024, 8, 19, 9, 30, 15,1, 0, 0)
time_str = time.asctime(time_tuple)     # Menampilkan format waktu dalam tuple menjadi mudah dibaca dan rapi
time_strmk = time.mktime(time_tuple)    # Menampilkan jarak berapa detik waktu dalam tuple dengan waktu epoch
print(time_str)
print(time_strmk)