def mass():
    force_ = int(input("Введите силу: "))
    acceleration = int(input("Введите ускорение: "))
    if acceleration!=0:
        mass = force_/acceleration
        print(f"{mass} кг")
    else:print("Ошибка: ускорение равно нулю")
mass()