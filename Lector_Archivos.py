#Lector de archivos

import hashlib
import os
from datetime import datetime

sha = hashlib.sha256()

def log(archivo):
    now = datetime.now()
    with open("./almacenamiento/log.txt", 'a') as file:
        file.writelines(now.date() ' - ' + now.time() + " -> El fichero: " + archivo + " ha sido modificado")

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




def comp_hash(filename, almacenamiento):
    ruta=filename.split('/')
    nombre=ruta[-1]
    hash=hash_file(filename)
    archivo=open(almacenamiento, 'r')
    lineas=archivo.readlines()
    lista=[]  
    lista_hash=[]
    for linea in lineas:
        trozos=linea.split(':')
        lista.append(trozos[0])
        lista_hash.append(trozos[1])
        
    if nombre in lista:
        if not (hash in lista_hash):
            log(nombre)

    else:
        with open(almacenamiento, 'a') as file:
            file.writelines(nombre+':'+hash+'\n')


#escritura(".\\almacenamiento\\prueba.txt")

comp_hash('./archivos/a.txt', './almacenamiento/prueba.txt')