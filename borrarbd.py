import sqlite3
def borrabd():
    conexion= sqlite3.connect("hashbase.db")
    conexion.execute("""drop table if exists ficheros""")

borrabd()