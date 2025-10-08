import task1
import task2
import task3
import task4
import task5
import task6
import task7
import task8
import task9
import task10
def main():
    while True:
        print("="*40)
        print("Выберите задачу:")
        print("1. Определение скорости")
        print("2. Определение массы")
        print("3. Определение температуры по Цельсию")
        print("4. Определение работы")
        print("5. Определение кинетической энергии")
        print("6. Определение потенциальной энергии")
        print("7. Определение давлени")
        print("8. Определение теплоты")
        print("9. Определение частоты")
        print("10. Определение объема")
        print("q. Выход")
        print("="*40)
        
        choice = input("Ваш выбор: ").strip()

        if choice == "q":
            print("Выход из программы.")
            break
        elif choice == "1":
            task1.speed()
        elif choice == "2":
            task2.mass()
        elif choice == "3":
            task3.temp()
        elif choice == "4":
            task4.work()
        elif choice == "5":
            task5.energy()
        elif choice == "6":
            task6.pot_energy()
        elif choice == "7":
            task7.press()
        elif choice == "8":
            task8.qofheat()
        elif choice == "9":
            task9.frequency()
        elif choice == "10":
            task10.volume()
       
        else:
            print("Некорректный ввод. Введите 1 или q.")

if __name__ == "__main__":
    main()