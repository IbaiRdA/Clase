import base64
from Crypto.Util.number import *
import numpy as np

string = "label"

key = 13

codificado = [chr(ord(x)^key) for x in string]

flag = codificado

print(flag)