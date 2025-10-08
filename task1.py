def speed():
    distance = int(input("Введите расстояние: "))
    time = int(input("Введите время: "))
    if time!=0:
        velocity = distance/time
        print(f"{velocity} км/ч")
    else:print("Ошибка: время равно нулю")
speed()