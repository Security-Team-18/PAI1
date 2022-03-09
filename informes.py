import time
import hashlib
import os.path as path
import os
from pathlib import Path
import datetime
from Lector_Archivos import comp_hash

tipoDir = './archivos'

def hash_file(filename):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    sha256 = hashlib.sha256()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

def cicloCompletoDiario():

    contador,total= comp_hash(tipoDir)
    diario = contador/total*100
    fechaActual = datetime.datetime.now()
    log = open('./almacenamiento/logDiario.txt', 'a')
    log.write(str(fechaActual.year)+ '-' + str(fechaActual.month)+ '-' + str(fechaActual.day) + ' ' + str(fechaActual.hour) + ':' +  str(fechaActual.minute)+ ':' + str(fechaActual.second) + ' ' + str(diario) + ' ' + '%')
    log.write("\n")
    log.close()
    return diario

def elegirMes(fechaActual):
    if fechaActual.month == 1:
        return 'Enero'
    if fechaActual.month == 2:
        return 'Febrero'
    if fechaActual.month == 3:
        return 'Marzo'
    if fechaActual.month == 4:
        return 'Abril'
    if fechaActual.month == 5:
        return 'Mayo'
    if fechaActual.month == 6:
        return 'Junio'
    if fechaActual.month == 7:
        return 'Julio'
    if fechaActual.month == 8:
        return 'Agosto'
    if fechaActual.month == 9:
        return 'Septiembre'
    if fechaActual.month == 10:
        return 'Octubre'
    if fechaActual.month == 11:
        return 'Noviembre'
    if fechaActual.month == 12:
        return 'Diciembre'

fechaActual = datetime.datetime.now()

def cicloCompletoMensual():
    mensual = 0
    res = 0
    while res < 30:
        diario = cicloCompletoDiario()
        mensual = mensual + diario
        res = res + 1
        time.sleep(10)
    if res == 30:
        log = open("./almacenamiento/logMensual.txt", 'a')
        log.write("El porcentaje de archivos integros que estamos verificando en el mes de " +  elegirMes(fechaActual) + ' es del ' + str(mensual/30) + '%')
        log.write("\n")
        log.close()


cicloCompletoMensual()