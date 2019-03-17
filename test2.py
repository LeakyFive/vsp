Mesich = int(input("Введите номер месяца от 1 до 12: \n"))

if Mesich < 1:
    print("Номер месяца меньше 1!")
if Mesich > 12:
    print("Номер месяца больше 12!")

if Mesich >= 1:
    if Mesich <= 2:
        print("Зима")

if Mesich >= 3:
    if Mesich <= 5:
        print("Весна")

if Mesich >= 6:
    if Mesich <= 8:
        print("Лето")

if Mesich >= 9:
    if Mesich <= 11:
        print("Осень")

if Mesich >= 12:
    print("Зима")
