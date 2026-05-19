import json
from collections import Counter

BOOKS_FILE = "books.json"


# Загрузка книг
def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Сохранение книг
def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


# Добавление книги
def add_book(books):
    author = input("Введите автора: ")
    title = input("Введите название книги: ")

    # Проверка дубликатов
    for book in books:
        if (
            book["author"].lower() == author.lower()
            and book["title"].lower() == title.lower()
        ):
            print("Такая книга уже существует")
            return

    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))

            if 1 <= rating <= 5:
                break

            print("Оценка должна быть от 1 до 5")

        except ValueError:
            print("Введите число")

    read_date = input("Введите дату прочтения: ")

    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date": read_date
    }

    books.append(new_book)
    save_books(books)

    print("Книга добавлена")


# Показ всех книг
def show_books(books):
    if not books:
        print("Список книг пуст")
        return

    for index, book in enumerate(books, start=1):
        print(
            f"{index}. "
            f"{book['author']} — {book['title']} | "
            f"Оценка: {book['rating']} | "
            f"Дата: {book['date']}"
        )


# Средняя оценка
def average_rating(books):
    if not books:
        print("Нет данных для расчёта")
        return

    avg = sum(book["rating"] for book in books) / len(books)
    print(f"Средняя оценка: {avg:.2f}")


# Статистика по авторам
def author_statistics(books):
    if not books:
        print("Список книг пуст")
        return

    authors = Counter(book["author"] for book in books)

    print("Статистика по авторам:")

    for author, count in authors.items():
        print(f"{author}: {count} книг")


# Удаление книги
def delete_book(books):
    if not books:
        print("Список книг пуст")
        return

    show_books(books)

    try:
        index = int(input("Введите номер книги для удаления: ")) - 1

        if 0 <= index < len(books):
            removed = books.pop(index)
            save_books(books)

            print(f"Удалена книга: {removed['title']}")

        else:
            print("Неверный номер")

    except ValueError:
        print("Введите число")


# Главное меню
def main():
    books = load_books()

    while True:
        print("\nТрекер прочитанных книг")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            show_books(books)

        elif choice == "3":
            average_rating(books)

        elif choice == "4":
            author_statistics(books)

        elif choice == "5":
            delete_book(books)

        elif choice == "6":
            print("Выход из программы")
            break

        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()