import random
import my_module  #we are importing another python file here

random_integer = random.randint(1,10)
print(random_integer)

#0.000000 - 0.999999
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")


# print(my_module.pi)



