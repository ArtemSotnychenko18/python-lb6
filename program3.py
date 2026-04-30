import json

def main():
    # Словник 
    students = {
        "Коваленко": ["Олександр", "Іванович", 2003],
        "Шевченко": ["Марія", "Петрівна", 2004],
        "Ткаченко": ["Дмитро", "Сергійович", 2002],
        "Бойко": ["Анна", "Миколаївна", 2005],
        "Кравченко": ["Максим", "Володимирович", 2003],
        "Олійник": ["Софія", "Олегівна", 2004],
        "Мельник": ["Андрій", "Вікторович", 2002],
        "Мороз": ["Вікторія", "Тарасівна", 2003],
        "Лисенко": ["Ігор", "Олександрович", 2004],
        "Гриценко": ["Олена", "Василівна", 2005]
    }

    file_name = "students.json"

    # Запис у JSON файл

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(students, file, ensure_ascii=False, indent=4)
    print(f"Дані успішно записані у файл {file_name}.")

    # Читання з JSON файл
    print("\nЧитання даних з файлу:")
    with open(file_name, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)

    # Вивід прочитаних даних у консоль
    for surname, details in loaded_data.items():
        name = details[0]
        patronymic = details[1]
        year = details[2]
        print(f"Прізвище: {surname}, Ім'я: {name}, По батькові: {patronymic}, Рік народження: {year}")

if __name__ == "__main__":
    main()