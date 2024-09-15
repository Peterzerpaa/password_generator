import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Introduce la longitud de la contraseña: "))
a = ""
for i in range(longitud):
    a += random.choice(caracteres)
print("Tu contraseña generada es:", a)