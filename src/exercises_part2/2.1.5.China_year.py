year = int(input())
China_years = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]

China_years_corrected = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]

proceed_year = year % 12
match proceed_year:
    case 0:
        print(China_years_corrected[0])
    case 1:
        print(China_years_corrected[1])
    case 2:
        print(China_years_corrected[2])
    case 3:
        print(China_years_corrected[3])
    case 4:
        print(China_years_corrected[4])
    case 5:
        print(China_years_corrected[5])
    case 6:
        print(China_years_corrected[6])
    case 7:
        print(China_years_corrected[7])
    case 8:
        print(China_years_corrected[8])
    case 9:
        print(China_years_corrected[9])
    case 10:
        print(China_years_corrected[10])
    case 11:
        print(China_years_corrected[11])
    case _:
        print("Некорректный ввод")

