SECTIONS = {
    "1": "Студенты",
    "2": "Посещаемость",
    "3": "Статистика",
}


def open_section(title: str) -> None:
    print(f"\n{title}")
    print("0. Назад")
    while input("Выберите пункт: ").strip() != "0":
        print("Неизвестный пункт. Выберите 0, чтобы вернуться назад.")


def main() -> None:
    while True:
        print("\nAttendly")
        for number, title in SECTIONS.items():
            print(f"{number}. {title}")
        print("0. Выход")

        choice = input("Выберите пункт: ").strip()
        if choice == "0":
            return

        section = SECTIONS.get(choice)
        if section is None:
            print("Неизвестный пункт. Выберите номер из меню.")
        else:
            open_section(section)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print()
