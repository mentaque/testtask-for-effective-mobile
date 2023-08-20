import json

data_file = "contacts.json"


def load_data() -> list:
    """
    Загружает данные из файла и возвращает их в виде списка словарей.
    """
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data: list):
    """
    Сохраняет данные в файл в формате JSON.
    """
    with open(data_file, "w") as file:
        json.dump(data, file)


def display_contacts(page: int, page_size: int):
    """
    Выводит на экран контакты постранично.
    """
    data = load_data()
    start = (page - 1) * page_size
    end = start + page_size
    contacts_to_display = data[start:end]

    if not contacts_to_display:
        print("Нет данных для отображения.")
    else:
        for i, contact in enumerate(contacts_to_display, start=start + 1):
            print(
                f"{i}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']} ({contact['Название организации']})")


def add_contact():
    """
    Добавляет новый контакт в справочник.
    """
    data = load_data()
    contact = {
        "Фамилия": input("Введите фамилию: "),
        "Имя": input("Введите имя: "),
        "Отчество": input("Введите отчество: "),
        "Название организации": input("Введите название организации: "),
        "Телефон рабочий": input("Введите рабочий телефон: "),
        "Телефон личный": input("Введите личный телефон: ")
    }
    data.append(contact)
    save_data(data)
    print("Контакт успешно добавлен.")


def edit_contact():
    """
    Редактирует существующий контакт в справочнике.
    """
    data = load_data()
    contact_index = int(input("Введите номер контакта в телефонной книжке для редактирования: ")) - 1

    if 0 <= contact_index < len(data):
        contact = data[contact_index]
        print(f"Текущая информация: {contact}")
        field_to_edit = input("Введите поле для редактирования: ")
        new_value = input(f"Введите новое значение для поля '{field_to_edit}': ")
        contact[field_to_edit] = new_value
        save_data(data)
        print("Контакт успешно отредактирован.")
    else:
        print("Контакт с указанным номером не найден.")


def search_contacts():
    """
    Выполняет поиск контактов по характеристике.
    """
    data = load_data()
    search_term = input("Введите характеристику для поиска: ")
    search_results = []

    for contact in data:
        for key, value in contact.items():
            if search_term.lower() in value.lower():
                search_results.append(contact)

    if search_results:
        print("Результаты поиска:")
        for i, contact in enumerate(search_results, start=1):
            print(
                f"{i}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']} ({contact['Название организации']})")
    else:
        print("По вашему запросу ничего не найдено.")


while True:
    print("\nМеню:")
    print("1. Вывести контакты")
    print("2. Добавить контакт")
    print("3. Редактировать контакт")
    print("4. Поиск контактов")
    print("5. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        page = int(input("Введите номер страницы: "))
        page_size = int(input("Введите количество контактов на странице: "))
        display_contacts(page, page_size)
    elif choice == "2":
        add_contact()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        search_contacts()
    elif choice == "5":
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
