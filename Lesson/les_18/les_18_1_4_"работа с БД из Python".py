import psycopg2

# """ создаем подключение(connect) к БД """
# conn = psycopg2.connect(
#     host='localhost',
#     database='user_db',
#     user='postgres',
#     password='postgres'
# )
#
# """ вызываем переменную курсор """
# cur = conn.cursor()
#
# """ делаем запросы - execute query"""
# cur.execute("INSERT INTO user_account VALUES (%s, %s)",(3, "Max")) # добавление данных
# cur.executemany("INSERT INTO user_account VALUES (%s, %s)", [(8, "Anna"), (9, "Mars"), (10, "Bob")]) # добавление списка данных
# cur.execute("SELECT * FROM user_account") # вывод данных в консоль
#
# """ создать коммит """
# conn.commit()
#
# """ получить данные в Python """
# rows = cur.fetchall()
#
# """ вывести полученные данные """
# for row in rows:
#     print(row)
#
# """ закрыть курсор"""
# cur.close()
#
# """ закрыть соединение"""
# conn.close()

### ----- усовершенствуем вышеизложенное __________ усовершенствуем вышеизложенное ______
# with psycopg2.connect(host='localhost', database='user_db', user='postgres', password='postgres') as conn:
#     with conn.cursor() as cur:
#         # execute query
#         cur.execute("INSERT INTO user_account VALUES (%s, %s)", (11, "Marta"))
#         cur.execute("SELECT * FROM user_account")
#
#         rows = cur.fetchall()
#         for row in rows:
#             print(row)
#
# conn.close()

### ----- продолжаем улучшать работу с базой данных в Python ---------------
conn = psycopg2.connect(host='localhost', database='user_db', user='postgres', password='postgres')

try:
    with conn:
        with conn.cursor() as cur:
            # execute query
            cur.execute("INSERT INTO user_account VALUES (%s, %s)", (12, "Stiv"))

            cur.execute("SELECT * FROM user_account")
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()