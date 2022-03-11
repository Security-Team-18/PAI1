import sqlite3
import os
import hashing

def escritura():
    conexion= sqlite3.connect("hashbase.db")
    conexion.execute("""create table if not exists ficheros(
        nombre text primary key,
        hash text
    )""")
    ruta ='./archivos'
    contenido = os.listdir(ruta)
    for fichero in contenido:
        hash=hashing.hash_file(ruta+'/'+fichero)
        conexion.execute("insert into ficheros(nombre, hash) values (?,?)", (fichero, hash))
        conexion.commit()
    conexion.close()

escritura()