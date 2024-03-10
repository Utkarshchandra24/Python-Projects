#Day05: Password Generator
# This has 2 levels Easy level and Hard Level

# This is an Easy Level Code:-

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! \n")
pass_size = int(input("How many letters would you like in your password? \n"))
symbols_size = int(input("How many symbols would you like? \n"))
nums = int(input("How many numbers would you like? \n"))


print("\nHere is your password: ")

for ps in range(0,pass_size):
    print(letters[ps],end="")
for s in range(0,symbols_size):
    print(symbols[s],end="")
for n in range(0,nums):
    print(numbers[n],end="")

