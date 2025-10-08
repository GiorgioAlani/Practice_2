import math
def volume():
    radius = float(input("Введите радиус основания в метрах: "))
    height = float(input("Введите значение высоты в метрах: "))
    volume = math.pi * (radius**2)*height
    print(f"Вычисленный обьем: {round(volume,2)} м^3")
#volume()