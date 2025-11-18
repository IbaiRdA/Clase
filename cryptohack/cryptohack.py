
import base64

#-----------------------------------------------
# How to Solve this Roman emperor's cipher?
print("https://www.dcode.fr/caesar-cipher")

#-----------------------------------------------
print("crypto{y0ur_f1rst_fl4g}")

#-----------------------------------------------
# Given hex string
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Convert hex to bytes
byte_data = bytes.fromhex(hex_string)

# Step 2: Encode the bytes to Base64
base64_encoded = base64.b64encode(byte_data)

# Step 3: Convert bytes to string for readability
base64_string = base64_encoded.decode('ascii')

print(base64_string)
#-----------------------------------------------
# Given array of ASCII codes
ascii_numbers = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Convert each number to its corresponding ASCII character and join them into a string
flag = ''.join(chr(num) for num in ascii_numbers)

print(flag)

#-----------------------------------------------
# Given hex-encoded flag
hex_flag = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert hex to bytes, then decode to ASCII
flag = bytes.fromhex(hex_flag).decode('ascii')

print(flag)

#-----------------------------------------------

# Given hex string
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Convert hex to bytes
byte_data = bytes.fromhex(hex_string)

# Step 2: Encode the bytes to Base64
base64_encoded = base64.b64encode(byte_data)

# Step 3: Convert bytes to string for readability
base64_string = base64_encoded.decode('ascii')

print(base64_string)