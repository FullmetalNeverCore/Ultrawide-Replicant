import os
import re



file = input("Full path to NieR Replicant ver.1.22474487139.exe: ")
f_v = input("Input hex value of aspect ratio(example. 8E E3 18 40 ==> 8ee31840): ")
inst = "398ee33f"

def hex_get(filepath):
    with open(filepath,'rb') as f:
        cont = f.read().hex()
    contredact = cont.replace(inst, str(f_v))
    repfix = bytearray.fromhex(contredact)
    bo = open(filepath,'wb')
    bo.write(repfix)
    print("Ready!")


print("@!#!@#!@")
if re.search(r'[\s]', f_v):
    sys.exit("Write formatted value like in the example!")
else:
    hex_get(file)