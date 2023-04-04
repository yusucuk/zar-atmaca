import random
while True:
    print("Eğer zardaki sayıyı tutturursanız kazanırsınız")
    zarat = int(input("Zar atmak için 1'den 6'ya kadar bir sayı girin:"))
    zar = int(random.uniform(1, 7))
    print("Zar:")
    print(zar)

    if zarat == zar:
        print("KAZANDINIZ!!!")
    else:
        print("kaybettiniz :(")
