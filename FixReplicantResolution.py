import os
import re



file = input("Full path to NieR Replicant ver.1.22474487139.exe: ")
f_v = input("Input hex value of aspect ratio(example. 8E E3 18 40 ==> 8ee31840): ")


def hex_get(filepath):
    with open(filepath,'rb') as f:
        cont = f.read().hex()
    contredact = [cont[i:i+8] for i in range(0, len(cont), 8)]
    if "398ee33f" in contredact:
        print("True")
        print(contredact[1])
        data = [str(f_v) if x=="398ee33f" else x for x in contredact]
        print(data[1])
        if str(f_v) in data:
            print("True2")
            rep = ' '.join(data).replace(" ","")
            repfix = bytearray.fromhex(rep)
            bo = open(filepath,'wb')
            bo.write(repfix)
            print("Ready!")


print("@!#!@#!@")
if re.search(r'[\s]', f_v):
    sys.exit("Write formatted value like in the example!")
else:
    hex_get(file)