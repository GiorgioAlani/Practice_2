def mass():
    force_ = int(input("Введите силу в Ньютонах: "))
    acceleration = int(input("Введите ускорение в метрах на секунду в квадрате: "))
    if acceleration!=0:
        mass = force_/acceleration
        print(f"Вычисленная масса: {mass} кг")
    else:print("Ошибка: ускорение равно нулю")
#mass()