def energy():
    mass = float(input("Введите массу в кг: "))
    velocity = float(input("Введите скорость в метрах на секунду: "))
    energy = (mass * (velocity**2))/2
    print(f"Кинетическая энергия: {round(energy, 2)} Дж")
#energy()
    