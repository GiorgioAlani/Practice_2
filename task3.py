def temp():
    far = float(input("Введите температуру в граудусах Фаренгейта: "))
    cel = 5/9 * (far - 32)
    print(f"Температура в цельсиях: {round(cel, 2)} С")
temp()