import base64
from Crypto.Util.number import *
import numpy as np

code = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

#Es asociativa, sabiendo que el resultado empieza por "crypto{" podemos sacar la llave, lo que lleva a la flag completa

key = b"myXORkey"

#en repeticion para cubrir el hex
full_key = (key * (len(code) // len(key) + 1))[:len(code)]
result = bytes(c ^ k for c, k in zip(code, full_key))

print(result)