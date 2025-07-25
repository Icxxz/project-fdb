import psycopg2

def get_conection():
    return psycopg2.connect(
        dbname="ScreenHive",
        user="postgres",
        password="123451",
        host="localhost"
    )