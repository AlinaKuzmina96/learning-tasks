import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "rb") as ind:
     for line in ind:
         line = line.strip()
         try:
             s = simplecrypt.decrypt(line, encrypted)
         except simplecrypt.DecryptionException:
             continue

print(s.decode("utf-8"))
