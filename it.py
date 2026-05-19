# a=int(input())
# b=int(input())
# c=a+b
# d=a*b
# print('суммааэc,d)

# #
# # a=(4,5,67,5,6,4,54,64,5,3,6,5336,4,6874,3,6546,8,745,6,543)
# # for i in a:
# #     if i10:
# #          print(i)
#
# # name = input("What is your name?")
# # first_name = input("What is your first name?")
# # print("htllorf", name + " " + first_name)
#
# a=int(input("entry killometrs"))
# b=a*1000
# # print("metres",b)
#
# a=int(input("vedite chislo:"))
# if a%3==0:
#     print('delitsa na 3')
# # elif a%3==1:
# #     print('ne delitsa na 3')
#
# a=input("vvedite chislo")
# b=input("vvedite chislo")
# c=input("vvedite chislo")
# # d=input("vvedite chislo")
# # maximum=max(a,b,c,d)
# # print("maximum",maximum)
# #
# # a=0
# # while a<101:
# #     print(a)
# #     a=a+1
# #     b=a%2==0
# #     print(b)
#
# a=input("vvedite slovo")
# b=a.count('a')
# print(b)

# a=[3,2,32,4,24,5,46,654,45,67,6545,67,76,54,33,232,2,4,32,343]
# # for i in a:
# # a.sort()
# b=a[1:19:2]
# print(b)
#
# people=[
#     {"name":"boris",'age':'23' },
#     { "name":"john",'age':'24' },
#     {   "name":"john",'age':'25' },
#     {   "name":"john",'age':'26' }]
# sort=sorted(people,key=lambda x:x['age'],reverse=True)
# print(sort)
#
# #
# numbers = [15, 8, 23, 42, 17, 3, 45,4,656,4,6,3,5,4,23,46,43,6,3,4565,429]
# mum = numbers[0]
# for num in numbers[1:]:
#     if num > mum:
#         mum = num
#
# # print(f"Максимальное число: {mum}")
#
#
# # Создаём лямбда‑функцию
# is_positive = lambda x: x > 0
#
# # Тестируем с разными числами
# print(is_positive(4))
# print(is_positive(-3))
# # print(is_positive(0))
# # print(is_positive(3.14))
#
# lst = ["apple", "banana", "cherry", "date", "elderberry",'42']
# lst2=[]
# for i in lst:
#     lst2.append(len(i))
# # print(lst2)
#
# dr=0
# a=0
# while a<101:
#     dr=dr+a
#     a=a+1
# print(dr)

# #     for number in args:
# #         print(number)
# # print_numbers(1, 2, 3, 4, 5)
#
# def find_maximum(*nem):
#     return max(nem)
# print(find_maximum(213423,4234,345,44,14,12,123,))
# def extract_categories(categories, parent_path=''):
# # def print_numbers(*args):
#
#     paths = []  # Здесь будем хранить все пути
#
#     for category_name, subcategories in categories.items():
#         # Создаём текущий путь: либо просто название категории, либо добавляем к родительскому пути
#         if parent_path:
#             current_path = f"{parent_path} > {category_name}"
#         else:
#             current_path = category_name
#
#         # Добавляем текущий путь в список результатов
#         paths.append(current_path)
#
#         # Если у категории есть подкатегории (словарь не пустой), обрабатываем их
#         if subcategories:
#             # Рекурсивно вызываем функцию для подкатегорий, передавая текущий путь как родительский
#             sub_paths = extract_categories(subcategories, current_path)
#             # Добавляем все найденные подкатегории в общий список
#             paths.extend(sub_paths)
#
#     return paths  # Возвращаем полный список путей
#
#
# # Пример структуры категорий
# categories = {
#     "Электроника": {
#         "Телефоны": {
#             "Смартфоны": {},
#             "Проводные": {}
#         },
#         "Компьютеры": {
#             "Ноутбуки": {},
#             "Стационарные": {
#                 "Игровые": {},
#                 "Для работы": {}
#             }
#         }
#     },
#     "Одежда": {
#         "Мужская": {
#             "Джинсы": {},
#             "Куртки": {}
#         }
#     }
# }
#
# # Вызов функции без parent_path
# print("Без parent_path:")
# paths = extract_categories(categories)
# for path in paths:
#     print(path)
#
# print("\n" + "="*40 + "\n")
# #
# # # Вызов функции с parent_path = 'root'
# # print("С parent_path = 'root':")
# # paths_with_root = extract_categories(categories, 'root')
# # for path in paths_with_root:
# #     print(path)
# #
# #
# def extract_categories(categories, parent_path='', paths=None):
#     path=[]
#     for category, subcategories in categories.items():
#         if parent_path:
#             curent_path = f"{parent_path}>{category}"
#         else:
#             curent_path = category
#         path.append(curent_path)
#     if subcategories:
#         path.extend(extract_categories(subcategories, parent_path=curent_path))
#     return paths
#
# categories = {
#     "Электроника": {
#         "Телефоны": {
#             "Смартфоны": {},
#             "Проводные": {}
#         },
#         "Компьютеры": {
#             "Ноутбуки": {},
#             "Стационарные": {
#                 "Игровые": {},
#                 "Для работы": {}
#             }
#         }
#     },
#     "Одежда": {
#         "Мужская": {
#             "Джинсы": {},
#             "Куртки": {}
#         }
#     }
# }
#
# for path in extract_categories(categories, parent_path="root"):
#     print(path)

import collections

INITIAL_WORDS = [
    "арбуз", "банан", "весна", "город", "дверь", "енот", "жизнь", "завод",
    "игрок", "карта", "книга", "лампа", "метро", "налог", "океан", "пирог",
    "радио", "слово", "трава", "улица", "факел", "хомяк", "цапля", "чашка",
    "школа", "экран", "юрист", "ягода", "ручка", "мышка", "поезд", "рукав"
]


def calculate_letter_frequencies(words):

    frequencies = collections.Counter()
    for word in words:
        for letter in set(word):
            frequencies[letter] += 1
    return frequencies


def score_word(word, frequencies):
    return sum(frequencies[letter] for letter in set(word))


def filter_words(words, guess, exact, wrong_place):
    filtered = []
    for word in words:
        current_exact = sum(1 for w, g in zip(word, guess) if w == g)

        word_counts = collections.Counter(word)
        guess_counts = collections.Counter(guess)
        total_matches = sum((word_counts & guess_counts).values())

        current_wrong_place = total_matches - current_exact

        if current_exact == exact and current_wrong_place == wrong_place:
            filtered.append(word)

    return filtered


def main():
    print(" Компьютер угадывает ваше 5-буквенное слово.")
    print("Загадайте существительное из 5 букв (все буквы должны быть строчными).")

    possible_words = [w.lower() for w in INITIAL_WORDS if len(w) == 5]

    secret_word = input("Введите загаданное слово (программа его 'забудет'): ").strip().lower()
    while len(secret_word) != 5:
        secret_word = input("Слово должно быть строго из 5 букв! Попробуйте еще раз: ").strip().lower()

    attempts = 0

    while True:
        if not possible_words:
            print("Ошибка! Похоже, вы где-то ошиблись в подсчетах, или слова нет в словаре.")
            break

        frequencies = calculate_letter_frequencies(possible_words)
        guess = max(possible_words, key=lambda w: score_word(w, frequencies))

        attempts += 1
        print(f"\nПопытка №{attempts}: Компьютер говорит слово '{guess.upper()}'")

        if guess == secret_word:
            print(f"Компьютер угадал слово '{secret_word.upper()}' за {attempts} попыток!")
            break

        try:
            exact = int(input("Сколько букв угадано НА СВОИХ местах? "))
            wrong_place = int(input("Сколько букв угадано НЕ НА СВОИХ местах? "))
        except ValueError:
            print("Пожалуйста, вводите только числа.")
            attempts -= 1
            continue

        if exact == 5:
            print(f"Отлично! Слово '{guess.upper()}' угадано!")
            break

        possible_words = [w for w in possible_words if w != guess]
        possible_words = filter_words(possible_words, guess, exact, wrong_place)


if __name__ == "__main__":
    main()
