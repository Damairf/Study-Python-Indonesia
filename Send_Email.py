# Send Email Program
# Warning program ini memiliki resiko, setelah mengaktifkan less secure app acces akun anda, saya sarankan harus segera dinonaktifkan
# kembali setelah tidak menggunakan program ini
import smtplib

sender = "emailpengirim@gmail.com"
receiver = "emailpenerima@gmail.com"
password = "password pengirim"
subject = "Python send email"
body = "Halo Halo Bando"

# header
message = f"""From: Damai{sender}
To: Raya{receiver}
Subject: {subject}\n
{body}"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(sender, password)
    print("Logged in")
    server.sendmail(sender, receiver, message)
    print("Email sudah dikirim")
except smtplib.SMTPException as e:
    print("Nyalakan less secure app acces akun anda")