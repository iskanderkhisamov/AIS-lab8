print("Хисамов Искандер Равилевич 7281-11")
print("Лабораторная работа №8")

dictionary = {"квартира": "apartment",
              "собака": "dog",
              "корова": "cow",
              "свет": "light",
              "хорошо": "good",
              "европа": "europe",
              "привет": "hello",
              "длинный": "long",
              "прыжок": "jump",
              "мышь": "mice"}

while True:
    word = input("Слово: ")
    word = word.lower()
    if word == "выход":
        exit()
    if word in dictionary:
        print("Перевод:", dictionary.get(word))
    else:
        translate = input("В словаре нет этого слова, введите перевод: ")
        dictionary.setdefault(word, translate)
    print("Для выхода введите слово: выход")
