import base64

HEX_STRING = input("Veuillez rentrer la chaine hexadécimale à convertir : ")

BYTE_ARRAY = bytearray.fromhex(HEX_STRING)
print(BYTE_ARRAY)
BASE64_VAL = base64.b64encode(BYTE_ARRAY)
print(BASE64_VAL)