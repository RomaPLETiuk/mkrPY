def is_even_or_ends_with_seven(a, b):
    sum_ab = a + b
    abs_sum = abs(sum_ab)

    # Перевірка: чи парне число або чи закінчується на 7
    if abs_sum % 2 == 0:
        return f"|{a}+{b}| = {abs_sum}. Число є парним."
    elif abs_sum % 10 == 7:
        return f"|{a}+{b}| = {abs_sum}. Число закінчується цифрою 7."
    else:
        return f"|{a}+{b}| = {abs_sum}. Число не є парним і не закінчується на 7."

def translate_text(text, language):
    translations = {
        "uk": {
            "Мова: ": "Мова: ",
            "Ціле число a:": "Ціле число a:",
            "Ціле число b:": "Ціле число b:"
        },
        "en": {
            "Мова: ": "Language: ",
            "Ціле число a:": "Integer a:",
            "Ціле число b:": "Integer b:"
        }
    }
    return translations.get(language, translations['uk']).get(text, text)
