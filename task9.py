def frequency():
    period = float(input("Введите период в сеундах: "))
    if period !=0:
        frequency = 1/period
        print(f"Частота: {frequency} Гц")
    else:
        print("Ошибка: период равен нулю")
frequency()
        
  