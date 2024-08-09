# Rock Paper Scissors Game
import random
while True:
    pilihan = ["Kertas", "Batu", "Gunting"]
    bot = random.choice(pilihan)
    player = None

    while player not in pilihan:
        player = input("Pilih Kertas, Batu, Gunting: ").capitalize()
        
    if player == bot:
        print("Bot:", bot)
        print("Player:", player)
        print("Hasil Seri")
    elif player == "Batu":
        if bot == "Gunting" :
            print("Bot:", bot)
            print("Player:", player)
            print("Player Menang")
        if bot == "Kertas" :
            print("Bot:", bot)
            print("Player:", player)
            print("Bot Menang")
    elif player == "Kertas":
        if bot == "Gunting" :
            print("Bot:", bot)
            print("Player:", player)
            print("Bot Menang")
        if bot == "Batu" :
            print("Bot:", bot)
            print("Player:", player)
            print("Player Menang")
    elif player == "Gunting":
        if bot == "Batu" :
            print("Bot:", bot)
            print("Player:", player)
            print("Bot Menang")
        if bot == "Kertas" :
            print("Bot:", bot)
            print("Player:", player)
            print("Player Menang")
            
    rematch = None
    while rematch != "y" and rematch != "n":
        rematch = input("Apakah ingin bermain lagi? [y,n]: ").lower()
    if rematch == "y":
        print()
        print("Selamat Bermain")
    elif rematch == "n":
        print("Terima Kasih Sudah Bermain")
        break