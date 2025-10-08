def qofheat():
    mass = float(input("Введите массу в килограммах: "))
    udel = float(input("Введите значение удельной теплоемкости: "))
    deltat = float(input("Введите изменение темпертауры в цельсиях: "))
    heat = mass * udel * deltat
    print(f"Количество теплоты: {round(heat,2)} Дж")
#qofheat()
    