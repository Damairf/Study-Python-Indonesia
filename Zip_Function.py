# Zip Function
usernames = ["kominfo", "joshua", "sigma", "skibidi", "bawadehewok"]
password = ["admin1234", "susu_kambing", "kai_cenat", "toiletman", "ayampotong"]
login_date = ["1/1/2024", "2/1/2024", "3/1/2024", "4/1/2024"]

user_info_detail = zip(usernames, password, login_date)
print(type(user_info_detail))
print()

for i in user_info_detail:
    print(i)
print()

user_info = dict(zip(usernames, password))
print(type(user_info))

for key,value in user_info.items():
    print(key+" : "+value)