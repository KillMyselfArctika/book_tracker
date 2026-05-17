import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def show_menu():
    print("\n=== Трекер книг ===")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")


def main():
    while True:
        show_menu()

        choice = input("Выберите пункт: ")

        if choice == "1":
            print("Добавление книги")
        elif choice == "2":
            print("Список книг")
        elif choice == "3":
            print("Средняя оценка")
        elif choice == "4":
            print("Статистика")
        elif choice == "5":
            print("Удаление")
        elif choice == "6":
            print("Выход...")
            break
        else:
            print("Неверный ввод")


if name == "main":
    main()
