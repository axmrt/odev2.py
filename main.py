import random

saylar = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifer = int(input("kaç haneli olsun?"))

for i in range(sifer):
    print(random.choice(saylar), end="")
