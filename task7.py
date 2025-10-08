def press():
    force = float(input("Введите силу в ньютонах: "))
    square = float(input("Введите площадь в квадратных метрах: "))
    press = force/square
    print(f"Вычисленное давление: {round(press, 2)} Па")
#press()