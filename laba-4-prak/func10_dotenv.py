from dotenv import dotenv_values

def demo_dotenv():
    # Якщо .env немає, повернеться порожній словник
    settings = dotenv_values(".env")
    print("Змінні з .env:", settings if settings else "файл .env не створено")
