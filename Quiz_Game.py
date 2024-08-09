# Quiz Game
def new_game():
    tebakan = []
    tebakan_benar = 0
    no_pertanyaan = 1
    
    for key in pertanyaan:
        print(key)
        for i in jawaban[no_pertanyaan-1]:
            print(i)
        print()
        jawab_user = input("Masukkan jawaban: ").upper()
        tebakan.append(jawab_user)
        tebakan_benar += check_answer(pertanyaan.get(key), jawab_user)
        no_pertanyaan += 1
        print()
    
    show_score(tebakan_benar, tebakan)

def check_answer(jawaban, jawab_user):
    if jawab_user == jawaban:
        print("BENAR")
        return 1
    else :
        print("SALAH")
        return 0    

def show_score(tebakan_benar, tebakan):
    print("HASIL")
    print("Jawaban Benar:", end="")
    for i in pertanyaan:
        print(pertanyaan.get(i), end=" ")
    print()
    print("Jawaban Anda:", end="")
    for i in tebakan:
        print(i, end=" ")
        
    print()
    score = int((tebakan_benar/len(pertanyaan))*100)
    print("Skor anda adalah "+str(score)+"%")
    if score == 0:
        print("Goblok, jawaban anda salah semua")
    elif score == 100:
        print("Selamat, jawaban anda benar semua")

def play_again():
    print()
    respon = None
    while respon != "Y" and respon != "N":
        respon = input("Apakah anda ingin mengerjakan lagi? [Y/N]: ").upper()
    if respon == "Y":
        return True
    elif respon == "N":
        return False

pertanyaan = {'1. Siapa presiden Indonesia pertama? ':'B',
              '2. \"Persatuan Indonesia\" merupakan sila keberapa? ':'A',
              '3. Indonesia merdeka pada tahun berapa? ':'D',
              '4. Siapa presiden perempuan pertama Indonesia? ':'C'}

jawaban = [['A. B.J Habibie', 'B. Ir. Soekarno', 'C. Joko Widodo', 'D. Soeharto'],
           ['A. 3', 'B. 1', 'C. 4', 'D. 2'], 
           ['A. 1947', 'B. 1495', 'C. 1946', 'D. 1945'],
           ['A. RA Kartini', 'B. Puan Maharani', 'C. Megawati', 'D. Cut Nyak Dien']]

new_game()

while play_again():
    print("Selamat mengerjakan")
    new_game()
    
print("Sampai Jumpa")