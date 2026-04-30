import re
import json
import urllib.parse
import pyperclip

#СОРТУВАННЯ 
#списки алфавітів
ua_alpha = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
en_alpha = "abcdefghijklmnopqrstuvwxyz"

def my_sort_key(w):
    w = w.lower()
    key = []
    for char in w:
        if char in ua_alpha:
            key.append((0, ua_alpha.index(char))) # Укр - пріоритет 0
        elif char in en_alpha:
            key.append((1, en_alpha.index(char))) # Лат - пріоритет 1
        else:
            key.append((2, ord(char)))
    return key

# Читаємо файл 
try:
    with open("text.txt", "r", encoding="utf-8") as f:
        content = f.read()
except:
    print("Файл не знайдено")
    exit()

print("текст із файлу:", content)

# Шукаємо слова
all_words = re.findall(r"\w+", content)
unique_words = list(set(all_words))
unique_words.sort(key=my_sort_key)

print("\nВідсортовані слова -", unique_words)