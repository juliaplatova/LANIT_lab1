import typer

def main(
    name: str,
    # Changed comment!!!
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    Added to comment on [master]
    """
    if formal: # Added to comment on [master]
        print(f"Добрый день, {name} {lastname}!") # Added to comment on [master]
    else: # Added to comment on [master]
        print(f"Привет, {name}!") # Added to comment on [master]


if __name__ == "__main__":
    typer.run(main)
