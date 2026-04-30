import urllib.parse 
import pyperclip

link = "https://uk.wikipedia.org/wiki/%D0%A8%D1%82%D1%83%D1%87%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82"
normal_link = urllib.parse.unquote(link)

print("\nURL було:", link)
print("URL стало:", normal_link)

try:
    pyperclip.copy(normal_link)
    print("Скопійовано в буфер обміну")
except:
    print("Помилка копіювання")