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
            add_book()
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


def add_book():
    books = load_books()

    author = input("Автор: ")
    title = input("Название: ")

    for book in books:
        if (
            book["author"].lower() == author.lower()
            and book["title"].lower() == title.lower()
        ):
            print("Такая книга уже существует")
            return

    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Введите число от 1 до 5")
        except ValueError:
            print("Введите число")

    date = input("Дата прочтения: ")

    new_book = {"author": author, "title": title, "rating": rating, "date": date}

    books.append(new_book)
    save_books(books)

    print("Книга добавлена")
def show_books():
    books = load_books()

    if not books:
        print("Список пуст")
        return

    for index, book in enumerate(books, start=1):
        print(
            f"{index}. "
            f"{book['author']} - "
            f"{book['title']} | "
            f"Оценка: {book['rating']} | "
            f"Дата: {book['date']}"
        )
def average_rating():
    books = load_books()

    if not books:
        print("Нет книг")
        return

    avg = sum(book["rating"] for book in books) / len(books)

    print(f"Средняя оценка: {avg:.2f}")
def author_stats():
    books = load_books()

    stats = {}

    for book in books:
        author = book["author"]
        stats[author] = stats.get(author, 0) + 1

    for author, count in stats.items():
        print(f"{author}: {count} книг")
if name == "main":
    main()
