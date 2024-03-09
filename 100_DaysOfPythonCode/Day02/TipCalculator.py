#Day02: Tip Calculator

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# print(type(bill))
# print(type(people))

split = bill/people
if percent==10:
    result = split*0.1
    perhead = split+result
elif percent==12:
    result = split*0.12
    perhead = split+result
elif percent==15:
    result = split*0.15
    perhead = split+result
else:
    perhead = split


# print("rounded the cost = ",round(perhead,2))


print("Each person should pay: $",round(perhead,2))

