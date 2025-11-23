import typer


def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):

    if formal:  # Если выбран формальный стиль флагом --formal или -f
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")


# Запуск приложения Typer из библиотеки Typer
typer.run(main)


