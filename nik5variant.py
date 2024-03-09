from datetime import datetime

# Функция для чтения данных из файла
def read_data_from_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                if len(parts) == 5:
                    start_time, end_time, received, sent, program = parts
                    data.append((start_time, end_time, int(received), int(sent), program))
                else:
                    print(f"Ошибка: некорректный формат строки в файле: {line.strip()}")
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
    return data

# Функция для вывода протокола использования сети Интернет программой Skype
def print_skype_protocol(data):
    skype_data = [entry for entry in data if entry[4] == "Skype"]
    if skype_data:
        print("Протокол использования сети Интернет программой Skype:")
        for entry in skype_data:
            print(f"Начало: {entry[0]}, Конец: {entry[1]}, Получено: {entry[2]}, Отправлено: {entry[3]}")
    else:
        print("Протокол использования сети Интернет программой Skype отсутствует.")

# Функция для вывода протокола использования сети Интернет после определенного времени
def print_protocol_after_time(data, target_time_str):
    try:
        target_time = datetime.strptime(target_time_str, "%H:%M:%S").time()
        print(f"Протокол использования сети Интернет после {target_time_str}:")
        for entry in data:
            start_time = datetime.strptime(entry[0], "%H:%M:%S").time()
            if start_time > target_time:
                print(f"Начало: {entry[0]}, Конец: {entry[1]}, Получено: {entry[2]}, Отправлено: {entry[3]}, Программа: {entry[4]}")
    except ValueError:
        print("Ошибка: некорректный формат времени. Используйте формат ЧЧ:ММ:СС.")

# Функция сортировки данных по времени (сортировка вставками)
def insertion_sort_by_time(data):
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x[0], "%H:%M:%S"))
    print("Сортировка данных по времени (сортировка вставками):")
    for entry in sorted_data:
        print(f"Начало: {entry[0]}, Конец: {entry[1]}, Получено: {entry[2]}, Отправлено: {entry[3]}, Программа: {entry[4]}")

# Функция сортировки данных по программам и байтам (сортировка вставками)
def insertion_sort_by_program_and_bytes(data):
    sorted_data = sorted(data, key=lambda x: (x[4], x[2] + x[3]))
    print("Сортировка данных по программам и байтам (сортировка вставками):")
    for entry in sorted_data:
        print(f"Начало: {entry[0]}, Конец: {entry[1]}, Получено: {entry[2]}, Отправлено: {entry[3]}, Программа: {entry[4]}")

# Чтение данных из файла
file_path = "D:\\lab\\Information.txt"
data = read_data_from_file(file_path)

# Выбор действия
while True:
    choice = input("Выберите опцию:\n1. Вывести протокол использования сети Интернет программой Skype.\n2. Вывести протокол использования сети Интернет после определенного времени.\n3. Сортировка данных по времени (сортировка вставками).\n4. Сортировка данных по программам и байтам (сортировка вставками).\nq. Выйти\n")

    if choice == "1":
        print_skype_protocol(data)
    elif choice == "2":
        target_time_str = input("Введите время (ЧЧ:ММ:СС): ")
        print_protocol_after_time(data, target_time_str)
    elif choice == "3":
        insertion_sort_by_time(data)
    elif choice == "4":
        insertion_sort_by_program_and_bytes(data)
    elif choice.lower() == "q":
        break
    else:
        print("Ошибка: некорректный выбор. Пожалуйста, выберите опцию из списка.")
