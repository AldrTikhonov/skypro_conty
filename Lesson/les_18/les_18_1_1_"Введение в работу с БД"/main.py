import psycopg2
import csv

def fill_table_from_csv(table_name, file_name):
    conn = psycopg2.connect(
        dbname="courses",
        user="postgres",
        password="postgres",
        port="5432",
        host="localhost"
    )

    cursor = conn.cursor()

    with open(file_name) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        for row in csv_reader:
            query = f"INSERT INTO {table_name} ({", ".join(header)}) VALUES ({', '.join(["%s"] * len(row))})"
            cursor.execute(query, row)

    conn.commit()
    cursor.close()
    conn.close()

def main():
    fill_table_from_csv('students', 'data/students.csv')
    fill_table_from_csv('instructors', 'data/instructors.csv')
    fill_table_from_csv('courses', 'data/courses.csv')


if __name__ == "__main__":
    main()
