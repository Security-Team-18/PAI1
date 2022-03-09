import sys
import hashlib
import os.path as path
import os
from pathlib import Path

# BUF_SIZE is totally arbitrary, change for your app!
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
