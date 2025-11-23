import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    if formal:  # Если выбран формальный стиль флагом --formal или -f
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    # Запуск приложения Typer
    typer.run(main)

