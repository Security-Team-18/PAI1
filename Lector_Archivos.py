#Lector de archivos

import hashlib

sha = hashlib.sha256()


def hash_file(filename):

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            sha.update(chunk)

    return sha.hexdigest()

message = hash_file("C:\\Users\\alefr\\pyHIDS\\archivos\\c.txt")
print(message)