def energy():
    mass = float(input("Введите массу: "))
    velocity = float(input("Введите скорость: "))
    energy = (mass * (velocity**2))/2
    print(f"{round(energy, 2)} Дж")
energy()
    