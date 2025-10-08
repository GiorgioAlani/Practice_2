def speed():
    distance = int(input("Введите расстояние в метрах: "))
    time = int(input("Введите время в часах: "))
    if time!=0:
        velocity = distance/time
        print(f"Вычисленная скорость: {velocity} км/ч")
    else:print("Ошибка: время равно нулю")
speed()