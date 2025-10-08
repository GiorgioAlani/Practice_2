def pot_energy():
    mass = float(input("Введите массу: "))
    height = float(input("Введите высоту: "))
    acceleration = float(input("Введите ускорение свободного падения: "))
    pot_energy = mass * height * acceleration
    print(f"{round(pot_energy,2)} Дж")
pot_energy()