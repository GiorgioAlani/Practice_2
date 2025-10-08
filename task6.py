def pot_energy():
    mass = float(input("Введите массу в кг: "))
    height = float(input("Введите высоту в метрах: "))
    acceleration = float(input("Введите ускорение свободного падения: "))
    pot_energy = mass * height * acceleration
    print(f"Потенциальная энергия: {round(pot_energy,2)} Дж")
pot_energy()