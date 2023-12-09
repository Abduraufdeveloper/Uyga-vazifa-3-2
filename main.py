import random
son = random.randint(1,100)
print("men men 1 dan 100 gacha bolgan sonlarni ichidan bitta son oyladim xozir random bibliotekasi meni sonimni topishi kerak")

while True:
    guess = int(input("siz nechi deb oylaysiz : "))
    if guess > son :
        print("yoq bu son men oylagandan katta ")
    elif guess < son :
        print(" xato bu son men oylaganimdan  kichik ")

    elif guess == son :
        print(f"congratulations. {son } bu sonni men oylagan edim ")