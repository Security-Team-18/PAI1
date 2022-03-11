#Lector de archivos

import hashlib
import os
import sqlite3
from datetime import datetime
import hashing

sha = hashlib.sha256()


def log(archivo, valor):
    
    now = datetime.now()
    fecha=now.strftime("%d/%m/%Y %H:%M:%S")
    with open("./almacenamiento/log.txt", 'a') as file:
        file.writelines(fecha+ " -> El fichero: " + archivo + " ha sido " +valor+ "\n")

def comp_hash(path):
    conexion= sqlite3.connect("hashbase.db")
    cur= conexion.cursor()
    contenido= os.listdir(path)
    total= cur.execute("SELECT * FROM ficheros")
    total= len(cur.fetchall())
    res=0
    for filename in contenido:
        nombre=filename
        hash=hashing.hash_file(path+'/'+filename)
        busqueda=cur.execute("SELECT ficheros.hash FROM ficheros WHERE ficheros.nombre= ?", (nombre,))
        busqueda= cur.fetchall()
        if(len(busqueda)==0):
            log(nombre, 'insertado')
            total=total+1
        elif(busqueda[0][0]!=hash):
            log(nombre, 'modificado')
        else:
            res= res+1
    return res, total

        


