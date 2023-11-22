import os
from deep_translator import GoogleTranslator

def read_config_file():
    try:
        config = {}
        with open("config.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
        return config
    except Exception as e:
        return str(e)

def check_file_exists(filename):
    try:
        return os.path.isfile(filename)
    except Exception as e:
        return str(e)

def count_text_stats(text):
    try:
        num_characters = len(text)
        num_words = len(text.split())
        num_sentences = text.count('.') + text.count('!') + text.count('?')
        return num_characters, num_words, num_sentences
    except Exception as e:
        return str(e)

def translate_text():

    config = read_config_file()
    text_filename = config.get("text_file")
    target_language = config.get("target_language")
    output_destination = config.get("output_destination")
    max_characters = int(config.get("max_characters"))
    max_words = int(config.get("max_words"))
    max_sentences = int(config.get("max_sentences"))

    if not check_file_exists(text_filename):
        print(f"Файл '{text_filename}' не знайдено.")
        return

    with open(text_filename, "r") as file:
        text = file.read()

    num_characters, num_words, num_sentences = count_text_stats(text)

    print(f"Назва файла: {text_filename}")
    print(f"Розмір файла: {os.path.getsize(text_filename)} байт")
    print(f"Кількість символів: {num_characters}")
    print(f"Кількість слов: {num_words}")
    print(f"Кількість реченнь: {num_sentences}")
    print(f"Мова текста: {target_language}")

    if num_characters > max_characters or num_words > max_words or num_sentences > max_sentences:
        print("Досягнуто ліміт символів, слів або речень.")
        return

    translator = GoogleTranslator(source='auto', target=target_language)

    try:
        translation = translator.translate(text)
    except Exception as e:
        print(f"Помилка при перекладі: {e}")
        return

    if output_destination == "file":
        output_filename = f"translated_{target_language}.txt"
        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write(f"Мова переклада: {target_language}\n")
            output_file.write(translation)
        print("Ok")
    elif output_destination == "screen":
        print(f"Мова переклада: {target_language}")
        print(translation)
        print("Ok")
    else:
        print("Невідоме місце  виведення результату.")

translate_text()