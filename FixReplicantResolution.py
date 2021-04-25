import os
import mmap
import binascii



file = input("Full path to NieR Replicant ver.1.22474487139.exe: ")


def hex_get(filepath):
    with open(filepath,'rb') as f:
        cont = f.read().hex()
    contredact = [cont[i:i+8] for i in range(0, len(cont), 8)]
    if "398ee33f" in contredact:
        print("True")
        print(contredact[1])
        data = ["26b41740" if x=="398ee33f" else x for x in contredact]
        print(data[1])
        if "26b41740" in data:
            print("True2")
            finisheddata = ' '.join(data).replace(" ","")
            print("True3")
            with open(filepath,'wb') as fw:
                fw.write(finisheddata)
                print("Ready!")



hex_get(file)