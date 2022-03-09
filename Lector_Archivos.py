#Lector de archivos

import hashlib
import os
import sqlite3
from datetime import datetime

sha = hashlib.sha256()


def log(archivo):
    
    now = datetime.now()
    fecha=now.strftime("%d/%m/%Y %H:%M:%S")
    with open("./almacenamiento/log.txt", 'a') as file:
        file.writelines(fecha+ " -> El fichero: " + archivo + " ha sido modificado \n")

def hash_file(filename):

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            sha.update(chunk)

    return sha.hexdigest()

#message = hash_file("C:\\Users\\alefr\\pyHIDS\\archivos\\c.txt")
#print(message)


def escritura(filename):
    ruta ='./archivos'
    contenido = os.listdir(ruta)
    for fichero in contenido:
        hash=hash_file(ruta+'/'+fichero)
        archivo= open(filename, 'a')
        archivo.writelines(fichero+':'+hash+'\n')
        archivo.close() 
         
    archivo= open(filename, 'r')
    print(archivo.read())  
    archivo.close() 




def comp_hash(ruta, almacenamiento):
    contenido= os.listdir(ruta)
    for filename in contenido:
        nombre=filename
        hash=hash_file(ruta+'/'+filename)
        archivo=open(almacenamiento, 'r')
        lineas=archivo.readlines()
        lista=[]  
        lista_hash=[]
        for linea in lineas:
            trozos=linea.split(':')
            lista.append(trozos[0].rstrip("\n"))
            lista_hash.append(trozos[1].rstrip("\n"))
        if nombre in lista:
            if hash in lista_hash:
                print('Todo en orden')
            else:
                log(filename)
        else:
            with open(almacenamiento, 'a') as file:
                file.writelines(nombre+':'+hash+'\n')


#escritura('./almacenamiento/prueba.txt')

comp_hash('./archivos', './almacenamiento/prueba.txt')