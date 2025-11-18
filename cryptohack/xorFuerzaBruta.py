import base64
from Crypto.Util.number import *
import numpy as np

code = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for k in range(256):                     # probar claves 0–255
    result = bytes(c ^ k for c in code)  # XOR con un solo byte
    try:
        text = result.decode()           # intentar leer como texto
        print(k, text)
    except:
        pass