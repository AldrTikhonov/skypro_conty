import json

# # Создадим словарь с заданными ключами
# book_info = {
#     'title': 'Sherlok Holmel',
#     'autor': 'Arthur Conan Doyle',
#     'publication_year': 1887,
#     'genres': ['detective', 'novel']
# }

# # Преобразуем словарь в строку JSON с помощью метода dumps
# book_info_str = json.dumps(book_info)
# print(book_info_str)
# # -----------------------------------------------------------------

# # Преобразуем обратно строку в словарь с помощью метода loads (НУЖНО закомментировать исходный словарь)
# book_info_str = '{"title": "Sherlok Holmel", "autor": "Arthur Conan Doyle", "publication_year": 1887, "genres": ["detective", "novel"]}'
#
# book_info = json.loads(book_info_str)
# print(book_info)
# # --------------------------------------------------------------------

# # Запишем исходный словарь в файл JSON с помощью метода dump(НУЖНО раскомментировать исходный словарь)
# with open('data.json', 'w') as json_file:
#     json.dump(book_info, json_file)
# # ----------------------------------------------------------------------

# # Откроем ранее созданный файл JSON используем метод load для чтения данных обратно в объект Python(НУЖНО закомментировать исходный словарь)
# with open('data.json') as json_file:
#     book_info = json.load(json_file)
#
#     print(book_info)
