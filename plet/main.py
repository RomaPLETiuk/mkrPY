import os
import json
from utils import is_even_or_ends_with_seven, translate_text
from colorama import Fore, Style, init

# Ініціалізуємо бібліотеку для роботи з кольорами
init(autoreset=True)

# Шлях до файлу з даними
file_name = 'MyData.txt'

def read_data():
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                return data
        except (json.JSONDecodeError, IOError):
            return None
    return None

def write_data(data):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def get_input():
    # Запитуємо введення даних користувача
    a = int(input("Введіть ціле число a: "))
    b = int(input("Введіть ціле число b: "))
    language = input("Введіть мову інтерфейсу (uk/en): ").lower()

    # Записуємо дані у файл
    data = {'a': a, 'b': b, 'language': language}
    write_data(data)
    print(f"Дані збережено в файл {file_name}")

def main():
    # Читаємо дані з файлу
    data = read_data()

    if not data:
        # Якщо дані некоректні або файл не існує
        get_input()
        return

    a = data['a']
    b = data['b']
    language = data.get('language', 'uk')

    # Перевіряємо мову інтерфейсу
    if language not in ['uk', 'en']:
        language = 'uk'

    # Показуємо мову інтерфейсу4

    print(translate_text("Мова: ", language) + ("Українська" if language == 'uk' else "English"))
    
    # Виводимо числа кольорово
    print(translate_text("Ціле число a:", language), Fore.RED + str(a))
    print(translate_text("Ціле число b:", language), Fore.BLUE + str(b))

    # Результат
    result = is_even_or_ends_with_seven(a, b)
    print(Fore.GREEN + result)

if __name__ == '__main__':
    main()
