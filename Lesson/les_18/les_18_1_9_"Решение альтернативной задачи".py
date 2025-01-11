"""
Задача: 'Ведение в работу с базами данных'

1.s= Создать БД courses из консоли используя утилиту psql
2. Создать три таблицы в БД courses

    * Таблица students должна содержать следующие столбцы - id(целое число),
      first_name(строка до 100 символов), last_name(строка до 100 символов),
      email(строка до 255 символов)
      Обязательные для заполнения поля - все, кроме поля email

    * Таблица instructors должна содержать следующие столбцы - id (целое число),
      first_name (строка до 100 символов), last_name(строка до 100 символов),
      email(строка до 255 символов), scope(строка до 50 символов)
      Обязательные для заполнения поля - все, кроме поля email

    * Таблица courses должна содержать следующие столбцы - id (строка 4 символа),
      name(название курса), instructor_id(ссылка на поле id таблицы instructors),
      student-id(ссылка на поле id таблицы students), start_date(дата)
      Все поля являются обязательными
3. Написать скрипт на Python, который заполнит таблицы данными из csv-файлов
"""

###                           задача выполняется в командной строке

# user@Acer:~$ service postgresql status
# ● postgresql.service - PostgreSQL RDBMS
#      Loaded: loaded (/usr/lib/systemd/system/postgresql.service; enabled; preset: ena>
#      Active: active (exited) since Mon 2025-01-06 15:00:48 MSK; 5h 57min ago
#     Process: 1269 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
#    Main PID: 1269 (code=exited, status=0/SUCCESS)
#         CPU: 6ms
#
# янв 06 15:00:48 Acer systemd[1]: Starting postgresql.service - PostgreSQL RDBMS...
# янв 06 15:00:48 Acer systemd[1]: Finished postgresql.service - PostgreSQL RDBMS.
# user@Acer:~$ sudo -i -u postgres
# [sudo] пароль для user:
# postgres@Acer:~$ psql
# psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1))
# Type "help" for help.
#
# postgres=# CREATE DATABASE courses;
# CREATE DATABASE
# postgres=#


###               задача выполняется в pgadmin4

# CREATE TABLE students(
# 	id int PRIMARY KEY,
# 	first_name VARCHAR(100) NOT NULL,
# 	last_name VARCHAR(100) NOT NULL,
# 	emal VARCHAR(255)
# );
#
# CREATE TABLE instructors(
# 	id int PRIMARY KEY,
# 	first_name VARCHAR(100) NOT NULL,
# 	last_name VARCHAR(100) NOT NULL,
# 	email VARCHAR(255),
# 	scope VARCHAR(50) NOT NULL
# );
#
# CREATE TABLE courses(
# 	id int PRIMARY KEY,
# 	name VARCHAR(100) NOT NULL,
# 	instructor_id int NOT NULL,
# 	student_id int NOT NULL,
# 	start_date DATE NOT NULL,
# 	FOREIGN KEY (instructor_id) REFERENCES instructors(id),
# 	FOREIGN KEY (student_id) REFERENCES students(id)
# );