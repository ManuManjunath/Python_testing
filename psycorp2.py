import psycopg2

# To write to PGSQL -
with psycopg2.connect(database="learning", user="postgres", password="", host="localhost") as connection:
    with connection.cursor() as cursor:
        cursor.execute("insert into my_table values("col_1", 1, "One"))
# This way ensures auto commit and auto closing of connection

# To read from a table -
with psycopg2.connect(database="learning", user="postgres", password="", host="localhost") as connection:
    with connection.cursor() as cursor:
        cursor.execute("select * from my_table")
        get = cursor.fetchall()
        print(get)
# For more options, check dir(cursor)
