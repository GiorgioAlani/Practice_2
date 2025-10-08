def temp():
    far = float(input("Введите температуру в граудусах цельсия: "))
    cel = 5/9 * (far - 32)
    print(round(cel, 2))
temp()