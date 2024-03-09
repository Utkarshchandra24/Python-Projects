#Exercise043

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)

size = len(names)
print("size=",size)

payer = random.randint(0,size-1)
payer_name = names[payer]

print(f"{payer_name} is going to buy the meal today!")

